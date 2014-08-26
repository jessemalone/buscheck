from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import inspect
from sqlalchemy.orm import backref, relationship
from datetime import date,datetime
import json

db = SQLAlchemy()

class SerializeableModel :
    def to_dict(self,depth=1):
        result = {}
        mapper = inspect(self)
        for col in mapper.attrs:
            attr = getattr(self,col.key)
            to_dict = getattr(attr,'to_dict', None)
            if (callable(to_dict) and depth >= 0):
                result[col.key] = attr.to_dict(depth-1)
            elif (hasattr(attr,'__iter__') and depth > 0):
                result[col.key] = [item.to_dict(depth-1) for item in attr]
            elif(not callable(to_dict) and not hasattr(attr,'__iter__')):
                result[col.key] = attr
            else:
                continue
        return result

    def to_JSON(self):
        return json.dumps(self.to_dict())


class Agency(db.Model,SerializeableModel):
    
    __tablename__ = "agencies"

    id = db.Column(db.Integer, primary_key = True)
    agency_phone = db.Column(db.String(64))
    agency_fare_url = db.Column(db.String(255))
    agency_url = db.Column(db.String(255))
    agency_id = db.Column(db.String(64), index = True)
    agency_name = db.Column(db.String(128))
    agency_timezone = db.Column(db.String(64))
    agency_lang = db.Column(db.String(8))


class Calendar(db.Model,SerializeableModel):
    
    __tablename__ = "calendar"

    id = db.Column(db.Integer, primary_key = True)
    service_id = db.Column(db.String(64), index = True)
    start_date = db.Column(db.Date, index = True)
    end_date = db.Column(db.Date, index = True)
    monday = db.Column(db.Boolean)
    tuesday = db.Column(db.Boolean)
    wednesday = db.Column(db.Boolean)
    thursday = db.Column(db.Boolean)
    friday = db.Column(db.Boolean)
    saturday = db.Column(db.Boolean)
    sunday = db.Column(db.Boolean)

    @staticmethod
    def is_running(service_id):
        days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
        service = Calendar.query.filter_by(service_id = service_id).all()[0]
        print service.service_id
        print service.start_date
        print service.end_date
        print date.today()
        if (date.today() < service.start_date or date.today() > service.end_date):
                return False

        today = date.today().weekday()
        if (datetime.now().hour < 3):
            today = (today - 1) % 7
        print days[today]
        return getattr(service,days[today]) == 1

    @staticmethod
    def get_active():
        days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
        today = date.today()
        dow = days[today.weekday()]
        return Calendar.query.filter(Calendar.start_date <= today)\
            .filter(Calendar.end_date >= today)\
            .filter(getattr(Calendar,dow) == True)

class CalendarDate(db.Model,SerializeableModel):
    
    __tablename__ = "calendar_dates"

    id = db.Column(db.Integer, primary_key = True)
    service_id = db.Column(db.String(64), index = True)
    date = db.Column(db.Date, index = True)
    exception_type = db.Column(db.Integer)

class Route(db.Model,SerializeableModel):

    __tablename__ = "routes"

    id = db.Column(db.Integer, primary_key = True)    
    route_long_name = db.Column(db.String(128))
    route_type = db.Column(db.Integer)
    route_text_color = db.Column(db.String(6))
    route_color = db.Column(db.String(6))
    agency_id = db.Column(db.String(64), index=True)
    route_id = db.Column(db.String(64), index = True)
    route_url = db.Column(db.String(255))
    route_desc = db.Column(db.String(255))
    route_short_name = db.Column(db.String(128), index = True)

class Shape(db.Model,SerializeableModel):
    
    __tablename__ = "shapes"

    id = db.Column(db.Integer, primary_key = True)
    shape_id = db.Column(db.String(64), index = True)
    shape_pt_lat = db.Column(db.Float)
    shape_pt_lon = db.Column(db.Float)
    shape_pt_sequence = db.Column(db.Integer)
    shape_dist_traveled = db.Column(db.Float)

class Stop(db.Model,SerializeableModel):
    
    __tablename__ = "stops"

    id = db.Column(db.Integer, primary_key = True)
    stop_lat = db.Column(db.Float, index = True)
    wheelchair_boarding = db.Column(db.Boolean)
    stop_code = db.Column(db.Integer)
    stop_lon = db.Column(db.Float, index = True)
    stop_id = db.Column(db.String(64), index = True)
    stop_url = db.Column(db.String(255))
    parent_station = db.Column(db.String(128))
    stop_desc = db.Column(db.String(255))
    stop_name = db.Column(db.String(128))
    location_type = db.Column(db.Integer)
    zone_id = db.Column(db.Integer)

class StopTime(db.Model,SerializeableModel):
    
    __tablename__ = "stop_times"

    id = db.Column(db.Integer, primary_key = True)
    trip_id = db.Column(db.String(64), db.ForeignKey('trips.trip_id'), index = True)
    arrival_time = db.Column(db.String(8))
    arrival_time_hour = db.Column(db.Integer, index = True)
    arrival_time_minute = db.Column(db.Integer, index = True)
    arrival_time_second = db.Column(db.Integer, index = True)
    departure_time = db.Column(db.String(8))
    departure_time_hour = db.Column(db.Integer, index = True)
    departure_time_minute = db.Column(db.Integer, index = True)
    departure_time_second = db.Column(db.Integer, index = True)
    stop_id = db.Column(db.String(64), index = True)
    stop_sequence = db.Column(db.Integer)
    stop_headsign = db.Column(db.String(128))
    pickup_type = db.Column(db.Integer)
    drop_off_type = db.Column(db.Integer)
    shape_dist_traveled = db.Column(db.Float)

    @staticmethod
    def to_system_hour(hour):
        return hour + 24 if hour < 3 else hour

class Trip(db.Model,SerializeableModel):
    
    __tablename__ = "trips"

    id = db.Column(db.Integer, primary_key = True)
    block_id = db.Column(db.String(64), index = True)
    route_id = db.Column(db.String(64), index = True)
    direction_id = db.Column(db.Integer)
    trip_headsign = db.Column(db.String(128))
    shape_id = db.Column(db.String(64))
    service_id = db.Column(db.String(64))
    trip_id = db.Column(db.String(64))
    trip_short_name = db.Column(db.String(128))
    wheelchair_boarding = db.Column(db.Boolean)
    bikes_allowed = db.Column(db.Boolean)

    stop_times = relationship("StopTime",backref="trip")
