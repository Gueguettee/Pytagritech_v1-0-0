from turtle import delay
from base import *
from database import *
import datetime
import requests
import random


link = 'http://localhost:5000/data'

DATA_MIN = -5
DATA_MAX = 5

ID = 0

GAP = 0.01

N_DATA = 1


for n in range(0,N_DATA):
    new_data = data_sensor(
        id = ID, 
        time = datetime.datetime.today().isoformat(),
        data = float(random.randrange(DATA_MIN*1000,DATA_MAX*1000,GAP*1000))/1000)

    request_data = {'id':str(new_data.id),'time':str(new_data.time),'data':str(new_data.data)}
    response = requests.post(link, data=request_data)
