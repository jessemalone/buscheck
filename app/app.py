from flask import Flask,Response, request
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from models import db, Route, Stop, StopTime, Trip, Calendar
from sqlalchemy import and_, or_, orm
from time import strftime
from datetime import datetime
import json

def jsonify(stuff):
    return Response(response=json.dumps(stuff),headers=None,mimetype='application/json')

def get_app():
    app = Flask(__name__)
    # CAUTION: debug mode causes memory leak in sqlalchemy session.
    app.debug = True
    app.config['SQLALCHEMY_ECHO'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://buscheck:buscheck@127.0.0.1:5432/buscheck'
    return app


app = get_app()
db.init_app(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

@app.route('/stops')
def get_stops():
    stops = Stop.query.all()
    #print ([stop.to_dict() for stop in stops])
    return jsonify([stop.to_dict() for stop in stops])

@app.route('/routes')
def get_routes():
    routes = Route.query.all()
    return jsonify([route.to_dict() for route in routes])

@app.route('/stop/<stop_id>/trips/within_minutes/<minutes>')
def get_stop_trips(stop_id,minutes):
    minutes = int(minutes)
    hour = datetime.now().hour
    if hour < 3:
        hour = hour + 24

    hourd = 0
    minutes_over = 0
    if minutes > 60 - datetime.now().minute:
        minutes_over = minutes - (60 - datetime.now().minute)
        minutes = 60
        hourd = 1

    stop_times = StopTime.query.filter_by(stop_id=stop_id)
    if minutes_over > 0:
        stop_times = stop_times.filter(or_(and_(\
            StopTime.arrival_time_minute >= 0, \
            StopTime.arrival_time_minute <= minutes_over,
            StopTime.arrival_time_hour == hour+hourd),and_( \
            StopTime.arrival_time_minute > datetime.now().minute, \
            StopTime.arrival_time_minute <= 60,
            StopTime.arrival_time_hour == hour)))
    else:    
        stop_times = stop_times.filter(StopTime.arrival_time_hour == hour)\
            .filter(StopTime.arrival_time_minute > datetime.now().minute)\
            .filter(StopTime.arrival_time_minute <= minutes + datetime.now().minute)
        
    stop_times = stop_times.all()
    
    # prune list of trips not running today
    for i,stop_time in enumerate(stop_times):
        if (not Calendar.is_running(stop_time.trip.service_id)):
            stop_times.remove(stop_time)
    
    return jsonify([stop_time.to_dict() for stop_time in stop_times])

@app.route('/stop/<stop_id>/trips', methods = ['GET'])
def get_upcoming_trips(stop_id):
    limit = 3 if request.args.get('limit') == None else request.args.get('limit')
    current_minute = datetime.now().minute
    current_hour = StopTime.to_system_hour(datetime.now().hour)

    active_service_ids = [calendar.service_id for calendar in Calendar.get_active()]

    stop_times = StopTime.query.join(StopTime.trip).filter(StopTime.stop_id == stop_id)\
        .filter(Trip.service_id.in_(active_service_ids))\
        .filter(\
        or_(\
            and_(\
                StopTime.arrival_time_minute > current_minute,\
                    StopTime.arrival_time_minute <= 60,\
                    StopTime.arrival_time_hour == current_hour\
                    ),\
            StopTime.arrival_time_hour > current_hour\
            )\
         ).order_by(StopTime.arrival_time.asc()).limit(limit)\
         .options(orm.contains_eager(StopTime.trip,Trip.stop_times)).all()

    return jsonify([stop_time.to_dict() for stop_time in stop_times])


#@app.route('/stop/<stop_id>/next')
#def get_predictions(stop_id)

if __name__ == '__main__':
    manager.run()
