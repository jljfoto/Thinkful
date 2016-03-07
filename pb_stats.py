import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import collections


x = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]

c = collections.Counter(x)

print("collection is: {0}".format(c))

print "the mean of c is {0}".format(np.mean(x))
print "the standard devition of c is {0}".format(np.std(x))
exit()
data = [i.split(',') for i in x]

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

