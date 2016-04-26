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
			print df.iloc[t]
			print " "
