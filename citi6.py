import requests
from pandas.io.json import json_normalize

r = requests.get('http://www.citibikenyc.com/stations/json')
df = json_normalize(r.json()['stationBeanList'])

print df.head()
t = 0
max_rows = len(df.index) - 1
in_service = 0
not_in_service = 0
no_bikes = 0
test_stations = 0

mean_availableBikes = df['availableBikes'].mean()
mean_availableDocks = df['availableDocks'].mean()
median_availableBikes = df['availableBikes'].median()
median_availableDocks = df['availableDocks'].median()

mean_in_service_only = (df['statusValue'] == 'In Service')
service_mean_availableBikes = df[mean_in_service_only]['availableBikes'].mean()
service_mean_availableDocks = df[mean_in_service_only]['availableDocks'].mean()


#service_median_availableBikes = df[mean_in_service_only]['availableBikes'].median()
# OR
service_median_availableBikes = df[df['statusValue'] == 'In Service']['availableBikes'].median()

service_median_availableDocks = df[df['statusValue'] == 'In Service']['availableDocks'].median()
# OR
#service_median_availableDocks = df[mean_in_service_only]['availableDocks'].median()

for station in r.json()['stationBeanList']:
	for k in df['statusValue']:
		t = t + 1
		if t < max_rows:
			if df['statusValue'].iloc[t] == "Not In Service":
				prefix = '--NS----> '
				not_in_service = not_in_service + 1
			elif df['availableBikes'].iloc[t] < 1:
				prefix = '--NB----> '
				no_bikes = no_bikes + 1
			elif df['testStation'] is True:
				prefix = '--TS----> '
				test_stations = test_stations + 1
			else:
				prefix = '--------> '
				in_service = in_service + 1
			print "{}  id: {}  availableBikes: {}  availableDocks: {} totalDocks: {}  statusValue: {}".format(prefix, df['id'].iloc[t], df['availableBikes'].iloc[t], df['availableDocks'].iloc[t], df['totalDocks'].iloc[t], df['statusValue'].iloc[t])

print "\nIn Service: {}   Not In Service: {}  Total Stations: {}  Stations with no bikes: {}  Test Stations: {}".format(in_service, not_in_service, (not_in_service + in_service), no_bikes, test_stations)

print "\nAll:        Mean of Available Bikes: {}     Mean of Available Docks: {}".format(round(mean_availableBikes,5) , round(mean_availableDocks,5))
print "All:        Median of Available Bikes: {}       Median of Available Docks: {}".format(round(median_availableBikes,5) , round(median_availableDocks,5))
print "\nIn Service: Mean of Available Bikes: {}    Mean of Available Docks: {}".format(round(service_mean_availableBikes,5) , round(service_mean_availableDocks,5))
print "In Service: Median of Available Bikes: {}       Median of Available Docks: {}".format(round(service_median_availableBikes,5) , round(service_median_availableBikes,5))
