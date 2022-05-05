import sys
sys.path.append( './.' )
from base import *
from database import sensor


for num in range(0,1000):

    sensor_to_delete = sensor.query.get_or_404(num)

    try:
        db.session.delete(sensor_to_delete)
        db.session.commit()
    except:
        exit()
