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
    cur.execute('CREATE TABLE IF NOT EXISTS city_airport_reference (count INT, city TEXT, time  INT, temperature INT, UNIQUE (count, city,time,temperature))')

with con:
    cur.execute('CREATE TABLE IF NOT EXISTS city_airport_max (count INT, city TEXT, time  INT, max_temp INT, min_temp INT, mean INT, median INT, range INT, UNIQUE (count, city,time,max_temp, range))')

sql = "INSERT INTO city_airport_reference (count, city, time, temperature) VALUES (?,?,?,?)"
sql2 = "INSERT INTO city_airport_max (count, city, time, max_temp, min_temp, mean, median, range) VALUES (?,?,?,?,?,?,?,?)"

count = 0
for k,v in city_airports.items():
    print "Airport: {}  Coord: {}  Time: {} ".format(k,v, cur_time)
    for day in range(30):
        start_time=(datetime.datetime.now() - datetime.timedelta(days=day)).strftime("%Y-%m-%dT%T")
        #print "start_time: {}   type: {}\n".format(start_time,type(start_time))
        req_str='https://api.forecast.io/forecast/'+API_KEY+'/'+v+','+str(start_time)
	r = requests.get(req_str)
	#print "{}\n".format(req_str)
	df = json_normalize(r.json())
	#print "{}\n".format(df.columns)
        max = 0
        min = 0
	for i in df['hourly.data'][0]:
            count = count + 1
	    #print count, k, dt.fromtimestamp(i['time']).strftime('%Y-%m-%d %T'), i['temperature']
            with con:
	        cur.execute(sql,(count, k, dt.fromtimestamp(i['time']).strftime('%Y-%m-%d %T'),i['temperature']))

            if i['temperature'] > max:
               max = i['temperature']

            if i['temperature'] < min:
               min = i['temperature']
        
        mean=0
        median=0
        with con:
	    cur.execute(sql2,(count, k, dt.fromtimestamp(i['time']).strftime('%Y-%m-%d %T'),max,min,mean,median,(max-min)))

con.close()

exit()

#extract the column from the DataFrame and put them into a list
station_ids = df['id'].tolist() 

#add the '_' to the station name and also add the data type for SQLite
station_ids = ['_' + str(x) + ' INT' for x in station_ids]

#create the table
#in this case, we're concatenating the string and joining all the station ids (now with '_' and 'INT' added)
with con:
    cur.execute("CREATE TABLE available_bikes ( execution_time INT, " +  ", ".join(station_ids) + ");")

#take the string and parse it into a Python datetime object
exec_time = parse(r.json()['executionTime'])

with con:
    cur.execute('INSERT INTO available_bikes (execution_time) VALUES (?)', (exec_time.strftime('%s'),))

id_bikes = collections.defaultdict(int) #defaultdict to store available bikes by station

#loop through the stations in the station list
for station in r.json()['stationBeanList']:
    id_bikes[station['id']] = station['availableBikes']

#iterate through the defaultdict to update the values in the database
with con:
    for k, v in id_bikes.iteritems():
	cur.execute("UPDATE available_bikes SET _" + str(k) + " = " + str(v) + " WHERE execution_time = " + exec_time.strftime('%s') + ";")


