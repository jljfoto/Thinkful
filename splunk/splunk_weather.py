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
from pyHEC import PyHEC



API_KEY='2d98d7a43da74022adcee263c990a208'
token='D14453B5-FDEC-4A47-89D7-9E226CEEAE97'
headers={'Authorization': 'Splunk D14453B5-FDEC-4A47-89D7-9E226CEEAE97'}
port="8088"
uri = "http://localhost"+":"+port+"/services/collector/event"

cur_time=datetime.datetime.now().strftime('%m/%d/%Y %T.%f')

city_airports={"San Francisco": '37.6188056,-122.3754167',
	       "Detroit Metro": '42.2124167,-83.3533889',
               "Chicago O'Hare": '41.9773201,-87.9080059',
               "Phoenix Sky Harbor": '33.4342778,-112.0115833',
               "Washington Dulles": '38.9474444,-77.4599444',
               "Miami International": '25.7953611,-80.2901111',
               "Palm Beach International": '26.6831667,-80.0955833',
               "Kona International": '19.7387658,-156.0456314',
               "San Carlos": '37.5118549,-122.2495235'}

#city_airports={"San Francisco": '37.6188056,-122.3754167'}

hec = PyHEC(token, "http://localhost")
count = 0
for k,v in city_airports.items():
    print "Airport: {}  Coord: {}  Time: {} ".format(k,v, cur_time)
    for day in range(1):
        start_time=(datetime.datetime.now() - datetime.timedelta(days=day)).strftime("%Y-%m-%dT%T")
        #print "start_time: {}   type: {}\n".format(start_time,type(start_time))
        req_str='https://api.forecast.io/forecast/'+API_KEY+'/'+v+','+str(start_time)


	r = requests.get(req_str)
	event='{"sourcetype":"weather", "host":"API", "event": {"city":"'+k+'", '+r.content[1:]+'}'

        #print "event: |{}|\n\n".format(event)
        p = requests.post(uri, data = event, headers=headers)

        #print "status_code: {}   test: {}".format(p.status_code,p.text)
        #print hec.send(event)
	#print "{}\n".format(req_str)
	#df = json_normalize(r.json())
	#print "{}\n".format(df.columns)

exit()
