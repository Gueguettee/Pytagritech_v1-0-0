import datetime
import requests
import random

link = 'http://localhost:5000/data'

DATA_MIN = -5
DATA_MAX = 5

ID = 50

GAP = 0.01

while(1):

    id = ID
    timedate = datetime.datetime.today().isoformat()
    data = float(random.randrange(DATA_MIN*1000,DATA_MAX*1000,int(GAP*1000)))/1000

    request_data = {'id':str(id),'time':str(timedate),'data':str(data)}
    response = requests.post(link, data=request_data)
    print(response)
