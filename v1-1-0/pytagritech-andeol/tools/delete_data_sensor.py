import sys
sys.path.append( './.' )
from base import *
from database import N_DATA,data_sensor


for id in range(0,1000):

    all_data = db.session.query(data_sensor).filter_by(id = id).all()

    if len(all_data) > N_DATA:
        num_to_delete = len(all_data) - N_DATA

        for num in range(0,num_to_delete):
            data_sensor_to_delete = all_data[num]
            db.session.delete(data_sensor_to_delete)

try:
    db.session.commit()
except:
    print('error')
    exit()
