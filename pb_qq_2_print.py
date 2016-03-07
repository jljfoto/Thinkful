import numpy as np 
import scipy.stats as stats
import matplotlib.pyplot as plt

#plt.figure()
test_data = np.random.normal(size=1000)   
print "test_data={0}".format(test_data)
#graph1 = stats.probplot(test_data, dist="norm", plot=plt)
print "first"
#plt.show() #this will generate the first graph


plt.figure()
test_data2 = np.random.uniform(low=1.0, high=500.0,size=1000)   
print "test_data2={0}".format(test_data2)
graph2 = stats.probplot(test_data2, dist="norm", plot=plt)
print "second"
plt.show() #this will generate the second graph