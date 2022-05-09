import sys
#sys.path.append( './.' )
#from database import data_sensor
import datetime
import requests
import random


link = 'http://localhost:5000/data'

DATA_MIN = -5
DATA_MAX = 5

ID = 50
N_DATA = 10

GAP = 0.01


for n in range(0,N_DATA):
    #new_data = data_sensor(
    #   id = ID, 
    #    time = datetime.datetime.today().isoformat(),
    #    data = float(random.randrange(DATA_MIN*1000,DATA_MAX*1000,int(GAP*1000)))/1000)

    id = ID
    time = datetime.datetime.today().isoformat()
    data = float(random.randrange(DATA_MIN*1000,DATA_MAX*1000,int(GAP*1000)))/1000

    request_data = {'id':str(id),'time':str(time),'data':str(data)}
    response = requests.post(link, data=request_data)
    #requests.get(link,)
    #requests.post(link,)
    print(response)
