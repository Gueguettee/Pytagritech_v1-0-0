from attr import NOTHING
from base import *
from database import *


for num in range(1,1000):

    sensor_to_delete = capteur.query.get_or_404(num)

    try:
        db.session.delete(sensor_to_delete)
        db.session.commit()
    except:
        exit()
