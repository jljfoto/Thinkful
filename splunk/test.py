import commands
p=commands.getstatusoutput('scp ./test.py jonathon@jljfoto:/tmp/test.py 2>&1')
for i in p:
    if type(i) == int:
       if i == 0:
          ff = "SUCCESS"
       else:
          ff = "ERROR"
       #if i == 0:
       #   ff = "STDOUT"
       #if i == 1:
       #   ff == "STDIN"
       #if i == 2:
       #   ff = "STDERR"
       print "{}: {}".format(ff,i)
    if type(i) == str:
       print "data: {}".format(i)
