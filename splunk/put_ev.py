import time
import calendar
import requests
import time
import datetime
from datetime import datetime as dt
import collections
from dateutil.parser import parse 
from pandas.io.json import json_normalize
import pandas as pd
import numpy as np

API_KEY='2d98d7a43da74022adcee263c990a208'

SPLUNK_HTTP_EVENT_COLLECTOR_KEY='4E727120-75DD-4FB9-8DC1-C66559F024BD'

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

city_airports={"San Francisco": '37.6188056,-122.3754167',
	       "Detroit Metro": '42.2124167,-83.3533889'}

count = 0
for k,v in city_airports.items():
    print "Airport: {}  Coord: {}  Time: {} ".format(k,v, cur_time)
    for day in range(2):
        start_time=(datetime.datetime.now() - datetime.timedelta(days=day)).strftime("%Y-%m-%dT%T")
        #print "start_time: {}   type: {}\n".format(start_time,type(start_time))
        req_str='https://api.forecast.io/forecast/'+API_KEY+'/'+v+','+str(start_time)
	r = requests.get(req_str)
        req_str2='https://localhost:8088/'+'Authorization Splunk '+SPLUNK_HTTP_EVENT_COLLECTOR_KEY+' '+r.content
        p = requests.post(req_str2)
	print "get status: {}     post_status: {}\n".format(r.status, p.status)
	print "r.content: {}\n".format(r.content)

        #print count, k, dt.fromtimestamp(i['time']).strftime('%Y-%m-%d %T'), max, min, np.mean(temp_list), np.median(temp_list), abs(max-min), temp_list, hour_list
        
exit()
