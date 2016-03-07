import matplotlib.pyplot as plt
import numpy as np 
import scipy.stats as stats
import collections
import matplotlib.mlab as mlab


x = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]

c = collections.Counter(x)

print("collection is: {0}".format(c))

# calculate the number of instances in the list
count_sum = sum(c.values())
print("count_sum is: {0}".format(count_sum))

for k,v in c.iteritems():
  print("The frequency of number " + str(k) + " is " + str(float(v) / count_sum))

plt.boxplot(x)
plt.savefig("prob_box.png")

plt.hist(x, histtype='bar')
plt.savefig("prob_hist.png")

plt.figure()
graph1 = stats.probplot(x, dist="norm", plot=plt)
plt.savefig("prob_qq.png")


print "\nthe mean of x is {0}".format(np.mean(x))
print "the standard deviation of x is {0}".format(np.std(x))
print "the variance of x is {0}".format(np.var(x))

mean = np.mean(x)
variance = np.var(x) 

sigma = np.sqrt(variance) # this is the standard deviation
print "the sigma of x is {0}".format(sigma)
x = np.linspace(-3,3,100)
plt.plot(x,mlab.normpdf(x,mean,sigma))
plt.savefig("prob_dist.png")
