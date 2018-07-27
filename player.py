import pickle
import os
import time

SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
cache = open("/".join([SCRIPT_DIR,'badapple']),'rb')
data = pickle.load(cache)
keys = sorted(data.keys())
start_time = time.time()
for i, key in enumerate(keys):
  os.system("clear")
  print(data[key])
  delta_time = start_time + (1/30)*(i+100) - time.time() 
  time.sleep(0.03)
time2 = time.time()

