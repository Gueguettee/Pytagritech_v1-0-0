from base import *
from database import *


N_COLUMN = 10
N_LINE = 10

LAT0 = 46.414905
LONG0 = 6.279049

GAP = 0.0001

N_TOT = N_COLUMN * N_LINE

for line in range(0,N_LINE):
    for column in range(0,N_COLUMN):

        new_sensor = sensor(
            id = line*10+column, 
            lat = LAT0-GAP*line, 
            long = LONG0+GAP*column)

        try:
            db.session.add(new_sensor)
            db.session.commit()
        except:
            flash('Veuillez réessayer')
            print("error")
