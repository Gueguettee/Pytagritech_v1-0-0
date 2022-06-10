import sys
sys.path.append( './.' )
from base import *
from database import sensor


all_sensors = db.session.query(sensor).all()

for num in range(0,len(all_sensors)):

    sensor_to_delete = all_sensors[num]
    db.session.delete(sensor_to_delete)

try:
    db.session.commit()
except:
    exit()
