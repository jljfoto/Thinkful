import requests
from pandas.io.json import json_normalize

r = requests.get('http://www.citibikenyc.com/stations/json')
df = json_normalize(r.json()['stationBeanList'])

print df.head()
t = 0
max_rows = len(df.index) - 1
for station in r.json()['stationBeanList']:
	for k in df['statusValue']:
		t = t + 1
		if t < max_rows:
			if df['statusValue'].iloc[t] == "In Service":
				print "id: {}  availableBikes: {}  availableDocks: {} totalDocks: {}  statusValue: {}".format(df['id'].iloc[t], df['availableBikes'].iloc[t], df['availableDocks'].iloc[t], df['totalDocks'].iloc[t], df['statusValue'].iloc[t])
			else:
				print "----- > id: {}  availableBikes: {}  availableDocks: {} totalDocks: {}  statusValue: {}".format(df['id'].iloc[t], df['availableBikes'].iloc[t], df['availableDocks'].iloc[t], df['totalDocks'].iloc[t], df['statusValue'].iloc[t])
