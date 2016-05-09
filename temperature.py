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

API_KEY='2d98d7a43da74022adcee263c990a208'

cur_time=calendar.timegm(time.gmtime())

city_airports={"San Francisco": '37.6188056,-122.3754167',
	       "Detroit Metro": '42.2124167,-83.3533889',
               "Chicago O'Hare": '41.9773201,-87.9080059',
               "Phoenix Sky Harbor": '33.4342778,-112.0115833',
               "Washington Dulles": '38.9474444,-77.4599444',
               "Miami International": '25.7953611,-80.2901111',
               "Palm Beach International": '26.6831667,-80.0955833',
               "Kona International": '19.7387658,-156.0456314',
               "San Carlos": '37.5118549,-122.2495235'}

con = lite.connect('weather.db')
cur = con.cursor()

with con:
    cur.execute('CREATE TABLE IF NOT EXISTS city_airport_max (count INT, city TEXT, time  INT, max_temp INT, min_temp INT, mean INT, median INT, range INT, hourly_temps TEXT, hourly_times TEXT, UNIQUE (count, city,time,max_temp, range))')

sql2 = "INSERT INTO city_airport_max (count, city, time, max_temp, min_temp, mean, median, range,hourly_temps, hourly_times) VALUES (?,?,?,?,?,?,?,?,?,?)"

count = 0
for k,v in city_airports.items():
    print "\nAirport: {}  Coord: {}".format(k,v)
    for day in range(30):
        start_time=(datetime.datetime.now() - datetime.timedelta(days=day)).strftime("%Y-%m-%dT%T")
        #print "start_time: {}   type: {}\n".format(start_time,type(start_time))
        req_str='https://api.forecast.io/forecast/'+API_KEY+'/'+v+','+str(start_time)
	r = requests.get(req_str)
	#print "{}\n".format(req_str)
	df = json_normalize(r.json())
	#print "{}\n".format(df.columns)
        max = 0
        min = 300
	for i in df['hourly.data'][0]:

            temp_list = []
            for i in df['hourly.data'][0]: temp_list.append(i['temperature'])

            hour_list = []
            for i in df['hourly.data'][0]: hour_list.append(i['time'])

            for tt in temp_list:
                if tt > max:
                   max = tt
                if tt < min:
                   min = tt

        count = count + 1
        with con:
	     cur.execute(sql2,(count, k, dt.fromtimestamp(i['time']).strftime('%Y-%m-%d %T'),max,min,np.mean(temp_list),np.median(temp_list),abs(max-min),str(temp_list).strip('[]'),str(hour_list).strip('[]')))

        print count, k, dt.fromtimestamp(i['time']).strftime('%Y-%m-%d %T'), max, min, np.mean(temp_list), np.median(temp_list), abs(max-min)
        
con.close()

con = lite.connect('weather.db')
cur = con.cursor()

df = pd.read_sql_query("SELECT * FROM city_airport_max ORDER BY count",con,index_col='time')

max_range=0
max_city=0
max_day=''
temps=''
times=''
for i in df.index:
    if df['range'][i] > max_range:
       max_range=df['range'][i]
       max_city=df['city'][i]
       max_day=i
       temps=df['hourly_temps'][i]
       times=df['hourly_times'][i]
print "\n\n{} airport had the highest temperature variation of {} on {}".format(max_city, max_range, max_day)

hourly_temps=[]
for i in temps.split(","):
    hourly_temps.append(i)

hourly_times=[]
for i in times.split(","):
    hourly_times.append(i)

plt.bar(hourly_times, hourly_temps)
plt.show()

exit()
