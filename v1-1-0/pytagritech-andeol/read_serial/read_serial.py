import serial
import time # Optional (required if using time.sleep() below)
import re
import requests

import datetime
import matplotlib.pyplot as plt

# %% Voltage conversion

vbat_max = 3.3
vnum_max = 4095

conv_ratio = vbat_max / vnum_max

# %% Web
link = 'http://pytagritech.isc.heia-fr.ch/data2'
#link ='http://160.98.71.19:5000/data2'
#link = 'http://127.0.0.1:5000/data2'
# %% Serial   

com_port = "COM32"
baudrate = 115200

ser = serial.Serial(port=com_port, baudrate=baudrate)

# %% Regex

data_start = "ds"
data_stop = "de"

bat_pattern = " bs (.*?) be"

# %% Functions

def str_to_num_array(data_str):
    idx1 = data_str.index(data_start)
    idx2 = data_str.index(data_stop)
    
    return data_str[idx1 + len(data_start) + 1: idx2]
    
def sanitize_num_array(num_array):
    num_split = num_array.split(' ')
    num_clean = [n for n in num_split if n.isdigit()]
    return num_clean

def num_array_to_voltage(num_array):
    voltage_array = [float(n)*conv_ratio for n in num_array]
    return voltage_array
'''
def meas_to_dict(voltage_array):
    
    time_now = datetime.datetime.now()
    
    return {"date" : time_now,
            "data" : voltage_array}
'''
def meas_to_dict(voltage_array, bat_level):
    
    time_now = datetime.datetime.now()
    
    return {"date" : time_now,
            "data" : voltage_array,
            "battery" : bat_level}

# %% Loop

bat_lvl = ''
v = []

while (True):
    plt.close('all')
    # Check if incoming bytes are waiting to be read from the serial input 
    # buffer.
    # NB: for PySerial v3.0 or later, use property `in_waiting` instead of
    # function `inWaiting()` below!
    if (ser.inWaiting() > 0):
        # read the bytes and convert from binary array to ASCII
        data_str = ser.read(ser.inWaiting()).decode('ascii') 
        # print the incoming string without putting a new-line
        # ('\n') automatically after every print()
        
        #print(data_str, end='\n')
        
        # identify battery level
        if re.match(bat_pattern, data_str) is not None:
            bat_lvl = re.search(bat_pattern, data_str).group(1)
            #print(f"Battery : {bat_lvl}")

        # identify voltage array
        if (data_start in data_str) and (data_stop in data_str):

            # Clean data
            data_array = str_to_num_array(data_str)
            num_clean = sanitize_num_array(data_array)
            v = num_array_to_voltage(num_clean)
            
            plt.plot(v)
            plt.show()
            
        print("----------------")
        
        if (bat_lvl is not None) and (v is not None):
            d = meas_to_dict(v, bat_lvl)
            
            # POST
            response = requests.post(link, data=d)
            print(response)

    # Optional, but recommended: sleep 10 ms (0.01 sec) once per loop to let 
    # other threads on your PC run during this time. 
    time.sleep(0.01)
    
# %% Close
ser.close()
          
# %%

bat_pattern = " bs (.*?) be"
if re.match(bat_pattern, data_str) is not None:
    bat_lvl = re.search(bat_pattern, data_str).group(1)
    print(f"Battery : {bat_lvl}")