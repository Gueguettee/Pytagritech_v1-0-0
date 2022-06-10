from base import *


N_DATA = 10


class sensor(db.Model):
    id = db.Column(db.Integer,nullable=False,primary_key = True)
    lat = db.Column(db.Float,nullable=False)
    long = db.Column(db.Float,nullable=False)


    def __init__(self, id, lat, long):
        self.id = id
        self.lat = lat
        self.long = long

    def __repr__(self):
        return '<Sensor : id=%r, lat=%r, long=%r>' %(self.id,self.lat,self.long)


class data_sensor(db.Model):
    id = db.Column(db.Integer,db.ForeignKey('sensor.id'),nullable=False,primary_key=False)
    time = db.Column(db.String(26),nullable=False,primary_key=True)
    data = db.Column(db.Float)

    def __init__(self, id, time, data):
        self.id = id
        self.time = time
        self.data = data

    def __repr__(self):
        return '<Data sensor : id=%r, time=%s, data=%r>' %(self.id,self.time,self.data)


#To create database :
#python3
#from database import *
#db.create_all()

#to upload database :
#delete database and recreate it
