import matplotlib.pyplot as plt
import numpy as np 
import scipy.stats as stats
import collections

x  = np.random.uniform(low=100,high=100.5,size=1000)

c = collections.Counter(x)

print("collection is: {0}".format(c))

# calculate the number of instances in the list
count_sum = sum(c.values())
print("count_sum is: {0}".format(count_sum))

for k,v in c.iteritems():
  print("The frequency of number " + str(k) + " is " + str(float(v) / count_sum))

plt.boxplot(x)
plt.savefig("probbox.png")

plt.hist(x, histtype='bar')
plt.savefig("probhist.png")

plt.figure()
graph1 = stats.probplot(x, dist="norm", plot=plt)
plt.savefig("prob_qq_x.png")
