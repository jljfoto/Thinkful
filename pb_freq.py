import collections

testlist = [1, 4, 5, 6, 9, 9, 9]

c = collections.Counter(testlist)

print("collection is: {0}".format(c))

# calculate the number of instances in the list
count_sum = sum(c.values())
print("count_sum is: {0}".format(count_sum))

for k,v in c.iteritems():
  print("The frequency of number " + str(k) + " is " + str(float(v) / count_sum))
