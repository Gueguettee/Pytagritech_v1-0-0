from base import *

class sensor(db.Model):
    num = db.Column(db.Integer, primary_key = True)
    id = db.Column(db.Integer)
    lat = db.Column(db.Float)
    long = db.Column(db.Float)


    def __init__(self, id, lat, long):
        self.id = id
        self.lat = lat
        self.long = long

    def __repr__(self):
        return '<Sensor %r>' %self.num


#To create or upload database :
#python3
#from base import db
#db.create_all()