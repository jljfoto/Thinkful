import requests
from pandas.io.json import json_normalize

r = requests.get('http://www.citibikenyc.com/stations/json')
df = json_normalize(r.json()['stationBeanList'])

print df.head()
t = 0
for station in r.json()['stationBeanList']:
	for k in df['statusValue']:
		t = t + 1
		if t < 5:
			if k == "In Service":
				print k, df['stationName'][t:]
