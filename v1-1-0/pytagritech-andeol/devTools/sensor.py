import time

import datetime
import requests

import numpy as np

# link = 'http://127.0.0.1:5000/data2'
link = 'http://pytagritech.isc.heia-fr.ch/data2'

x = np.arange(0,4*np.pi,0.1)   # start,stop,step
y = np.sin(x)
print(y)

shift = 0

while 1:
    time.sleep(1)
    request_data = {'date':datetime.datetime.now(), 'data':y[shift : shift+14], 'battery':98.5}
    shift = (shift + 14) % len(y)
    # print(request_data)
    response = requests.post(link, data=request_data)
    print(response)
	