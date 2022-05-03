from base import *

class sensor(db.Model):
    id = db.Column(db.Integer,nullable=False,primary_key = True)
    lat = db.Column(db.Float,nullable=False)
    long = db.Column(db.Float,nullable=False)


    def __init__(self, id, lat, long):
        self.id = id
        self.lat = lat
        self.long = long

    def __repr__(self):
        return '<Sensor %r>' %self.id


class data_sensor(db.Model):
    id = db.Column(db.Integer,db.ForeignKey('sensor.id'),nullable=False,primary_key=True)
    time = db.Column(db.String(26),nullable=False)
    data = db.Column(db.Float)

    def __init__(self, id, time, data):
        self.id = id
        self.time = time
        self.data = data

    def __repr__(self):
        return '<Sensor data %r>' %self.num


#To create or upload database :
#python3
#from database import *
#db.create_all()
