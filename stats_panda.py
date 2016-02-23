import pandas as pd
from scipy import stats

data = '''Region,Alcohol,Tobacco
North,6.47,4.03
Yorkshire,6.13,3.76
Northeast,6.19,3.77
East Midlands,4.89,3.34
West Midlands,5.63,3.47
East Anglia,4.52,2.92
Southeast,5.89,3.20
Southwest,4.79,2.71
Wales,5.27,3.53
Scotland,6.08,4.51
Northern Ireland,4.02,4.56'''

data2= data.split('\n')

print "data\n{0}\n".format(data)
print "data2\n{0}\n".format(data2)

data = data.splitlines()

print "data\n{0}\n".format(data)

data = [i.split(',') for i in data]
print "data\n{0}\n".format(data)

column_names = data[0] # this is the first row
data_rows = data[1::] # these are all the following rows of data
df = pd.DataFrame(data_rows, columns=column_names)

print "df\n{0}".format(df)

# alcohol mean - 5.44
# tobacco mean - 3.44

df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)

print "Alcohol mean: my calc: {0}  python calc: {1}".format(5.44,df['Alcohol'].mean())
print "tobacco mean: my calc: {0}  python calc: {1}".format(3.44,df['Tobacco'].mean())


print "\nAlcohol median: python calc: {0}".format(df['Alcohol'].median())
print "tobacco median: python calc: {0}".format(df['Tobacco'].median())


print "\nAlcohol mode: python calc: {0}".format(stats.mode(df['Alcohol']))
print "tobacco mode: python calc: {0}".format(stats.mode(df['Tobacco']))

print "\nAlcohol min-max: python calc: {0}".format(max(df['Alcohol']) - min(df['Alcohol']))
print "tobacco min-max: python calc: {0}".format(max(df['Tobacco']) - min(df['Tobacco']))

print "\nAlcohol stdev: python calc: {0}".format(df['Alcohol'].std())
print "tobacco stdev: python calc: {0}".format(df['Tobacco'].std())

print "\nAlcohol variance: python calc: {0}".format(df['Alcohol'].var())
print "tobacco variance: python calc: {0}".format(df['Tobacco'].var())

