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

# print "data\n{0}\n".format(data)
# print "data2\n{0}\n".format(data2)

data = data.splitlines()

data = [i.split(',') for i in data]
# print "data\n{0}\n".format(data)

column_names = data[0] # this is the first row
data_rows = data[1::] # these are all the following rows of data
df = pd.DataFrame(data_rows, columns=column_names)

print "\nThe contents of panda(pd) is df\n\n{0}\n".format(df)

# alcohol mean - 5.44
# tobacco mean - 3.44

# mean, median, mode, range, variance, and standard deviation

df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)

# mean
print "\nThe mean for the Alcohol and Tobacco dataset is {0} and {1}".format(df['Alcohol'].mean(),df['Tobacco'].mean())

# median
print "\nThe median for the Alcohol and Tobacco dataset is {0} and {1}".format(df['Alcohol'].median(),df['Tobacco'].median())

# mode
print "\nThe mode for the Alcohol and Tobacco dataset is {0} and {1}".format(stats.mode(df['Alcohol']),stats.mode(df['Tobacco']))

# range
print "\nThe range for the Alcohol and Tobacco dataset is {0} and {1}".format((max(df['Alcohol']) - min(df['Alcohol'])), (max(df['Tobacco']) - min(df['Tobacco'])))

# variance
print "\nThe variance for the Alcohol and Tobacco dataset is {0} and {1}".format(df['Alcohol'].var(),df['Tobacco'].var())

# standard deviation
print "\nThe standard deviation for the Alcohol and Tobacco dataset is {0} and {1}".format(df['Alcohol'].std(),df['Tobacco'].std())

