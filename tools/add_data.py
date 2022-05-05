import sys
sys.path.append( './.' )
from database import data_sensor
import datetime
import requests
import random


link = 'http://localhost:5000/data'

DATA_MIN = -5
DATA_MAX = 5

ID = 4
N_DATA = 5

GAP = 0.01


for n in range(ID,N_DATA):
    new_data = data_sensor(
        id = n, 
        time = datetime.datetime.today().isoformat(),
        data = float(random.randrange(DATA_MIN*1000,DATA_MAX*1000,int(GAP*1000)))/1000)

    request_data = {'id':str(new_data.id),'time':str(new_data.time),'data':str(new_data.data)}
    response = requests.post(link, data=request_data)
    requests.get(link,)
    requests.post(link,)
    print(response)
