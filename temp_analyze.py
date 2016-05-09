import time
import calendar
import requests
import sqlite3 as lite
import time
import datetime
from datetime import datetime as dt
import collections
from dateutil.parser import parse
from pandas.io.json import json_normalize
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

con = lite.connect('weather.db')
cur = con.cursor()

def keywithmaxval(d):
    """Find the key with the greatest value"""
    return max(d, key=lambda k: d[k])

df = pd.read_sql_query("SELECT * FROM city_airport_max ORDER BY count",con,index_col='time')
#print df.columns

#print df.head()

max_range=0
max_city=0
max_day=''
temps=''
times=''
for i in df.index:
#    if df['range'][i] > max_range:
#       max_range=df['range'][i]
#       max_city=df['city'][i]
#       max_day=i
#       temps=df['hourly_temps'][i]
#       times=df['hourly_times'][i]
     print df['range'][i]
     print i
print "{}: {} airport had the highest temperature variation of {} on {}".format(i,max_city, max_range, max_day)

hourly_temps=[]
print temps
for i in temps.split(","):
    hourly_temps.append(i)

hourly_times=[]
for i in times.split(","):
    hourly_times.append(i)


#print "hourly_temps: {}".format(hourly_temps)
#print "\nhourly_times: {}".format(hourly_times)

plt.bar(hourly_times, hourly_temps)
plt.show()

exit()
