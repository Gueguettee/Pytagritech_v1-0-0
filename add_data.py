from base import *
from database import *


DATA_MIN = 0
DATA_MAX = 100

N_DATA = 100

for n in range(0,N_DATA):
    new_data = data_sensor(
        id = line*10+column, 
        data = ...)

    try:
        db.session.add(new_sensor)
        db.session.commit()
    except:
        flash('Veuillez réessayer')
        print("error")
