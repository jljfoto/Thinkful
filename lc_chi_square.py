from scipy import stats
import collections
import pandas as pd
import matplotlib.pyplot as plt

# Load the reduced version of the Lending Club Dataset
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
# Drop null rows
loansData.dropna(inplace=True)

# Calculate the unique number of open credit lines
freq = collections.Counter(loansData['Open.CREDIT.Lines'])
print "Open Credit Lines Data {0}\n".format(freq)

# Plot them
plt.figure()
plt.bar(freq.keys(), freq.values(), width=1)
plt.savefig('lc_open_credit_lines.jpg')

chi, p = stats.chisquare(freq.values())
print "The value of p is: {0}".format(p)
print "The value of chi is: {0}".format(chi)
