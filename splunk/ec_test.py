from pyHEC import PyHEC
import datetime

cur_time=datetime.datetime.now().strftime('%m/%d/%Y %T.%f')
token="D14453B5-FDEC-4A47-89D7-9E226CEEAE97"
hec = PyHEC('D14453B5-FDEC-4A47-89D7-9E226CEEAE97', "http://localhost")
#event='{"event": {"name":"jonathon","time":"'+cur_time+'"}'
#event = {"text":"this is a message in a bottle", "whatever_else":"blabla"}

event={"sourcetype":"testJSON", "host":"testhost","event": {'name':'jonathon','time':cur_time}}

print "cur_time: {}".format(cur_time)
print "token: {}".format(token)
print "hec: {}".format(hec)
print "event: {}\n\n\n\n".format(event)


print hec.send(event)

exit()
