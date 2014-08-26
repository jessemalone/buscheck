import sys

sys.path.append('..')
sys.path.append('.')

import string
import csv
from zipfile import ZipFile
from app.app import get_app
from app.models import db,Agency,Calendar,CalendarDate,Route,Shape,Stop,StopTime,Trip

app = get_app()
db.init_app(app)

def set_time_values(obj,field,value):
    hour = value[0:2]
    minute = value[3:5]
    second = value[6:8]
    setattr(obj,field+'_hour',hour)
    setattr(obj,field+'_minute',minute)
    setattr(obj,field+'_second',second)

def import_objects(fh,classname,fieldnames, log_field):
    reader = csv.reader(fh)
    reader.next() #skip header
    with app.app_context():
        classname.query.delete()
        for j,values in enumerate(reader):
            obj = classname()
            for i, field in enumerate(fieldnames):
                if (field == 'arrival_time' or field == 'departure_time'):
                    set_time_values(obj,field,values[i])
                if (values[i].strip() == ''):
                    setattr(obj,field, None)
                else:
                    setattr(obj,field,values[i].strip())
            print 'Adding ' + obj.__class__.__name__ + ' : ' +  getattr(obj,log_field)
            db.session.add(obj)
            if (j % 5000 == 0):
                db.session.flush()
                db.session.commit()
        db.session.flush()
        db.session.commit()

    
def import_agencies(fh):
    fieldnames = [
        "agency_phone",
        "agency_fare_url",
        "agency_url",
        "agency_id",
        "agency_name",
        "agency_timezone",
        "agency_lang"
        ]
    import_objects(fh, Agency, fieldnames, 'agency_name')

def import_calendars(fh):
    fieldnames = [
        "service_id",
        "start_date",
        "end_date",
        "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday",
        "saturday",
        "sunday"
        ]

    import_objects(fh,Calendar,fieldnames,'service_id')

def import_dates(fh):
    fieldnames = [
        "service_id",
        "date",
        "exception_type"
        ]
    import_objects(fh,CalendarDate,fieldnames,'date')

def import_routes(fh):
    fieldnames = [
        "route_long_name",
        "route_type",
        "route_text_color",
        "route_color",
        "agency_id",
        "route_id",
        "route_url",
        "route_desc",
        "route_short_name"
        ]
    import_objects(fh,Route,fieldnames,'route_short_name')

def import_shapes(fh):
    fieldnames = [
        "shape_id",
        "shape_pt_lat",
        "shape_pt_lon",
        "shape_pt_sequence",
        "shape_dist_traveled"
        ]
    import_objects(fh,Shape,fieldnames,'shape_id')

def import_stops(fh):
    fieldnames = [
        "stop_lat",
        "wheelchair_boarding",
        "stop_code",
        "stop_lon",
        "stop_id",
        "stop_url",
        "parent_station",
        "stop_desc",
        "stop_name",
        "location_type",
        "zone_id"
        ]
    import_objects(fh,Stop,fieldnames,'stop_name')

def import_stop_times(fh):
    fieldnames = [
        "trip_id",
        "arrival_time",
        "departure_time",
        "stop_id",
        "stop_sequence",
        "stop_headsign",
        "pickup_type",
        "drop_off_type",
        "shape_dist_traveled"
        ]
    import_objects(fh,StopTime,fieldnames,'stop_id')

def import_trips(fh):
    fieldnames = [
        "block_id",
        "route_id",
        "direction_id",
        "trip_headsign",
        "shape_id",
        "service_id",
        "trip_id",
        "trip_short_name",
        "wheelchair_borading",
        "bikes_allowed"
        ]

    import_objects(fh,Trip,fieldnames,'trip_headsign')
zippath = sys.argv[1]
zipfile = ZipFile(zippath)

print 'Importing agencies'
agenciesfile = zipfile.open('agency.txt','r')
import_agencies(agenciesfile)
agenciesfile.close()

print 'Importing calendars'
calendarsfile = zipfile.open('calendar.txt','r')
import_calendars(calendarsfile)
calendarsfile.close()

print "Importing dates"
calendardatesfile = zipfile.open('calendar_dates.txt','r')
import_dates(calendardatesfile)
calendardatesfile.close()

print 'Importing routes'
routesfile = zipfile.open('routes.txt','r')
import_routes(routesfile)
routesfile.close()

print 'Importing shapes'
shapesfile = zipfile.open('shapes.txt','r')
import_shapes(shapesfile)
shapesfile.close()

print 'Importing stops'
stopsfile = zipfile.open('stops.txt','r')
import_stops(stopsfile)
stopsfile.close()

print 'Importing stop times'
stoptimesfile = zipfile.open('stop_times.txt','r')
import_stop_times(stoptimesfile)
stoptimesfile.close()

print 'Importing trips'
tripsfile = zipfile.open('trips.txt','r')
import_trips(tripsfile)
tripsfile.close()

zipfile.close()
