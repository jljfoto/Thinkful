import time

for i in range(1,60):
	print "\nStart : %s" % time.ctime()
	time.sleep( 60 )
	print "End : %s" % time.ctime()
