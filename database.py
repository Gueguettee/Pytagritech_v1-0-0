from base import *

class capteur(db.Model):
    num = db.Column(db.Integer, primary_key = True)
    id = db.Column(db.Integer)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)


    def __init__(self, id, latitude, longitude):
        self.id = id
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):
        return '<Capteur %r>' %self.num

#mettre a jour la base de donnée, créer un nouveau tableau taper dans terminal : 
# python3
#from base import db
#db.create_all()