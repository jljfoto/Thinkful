import subprocess

def runProcess(exe):    
    p = subprocess.Popen(exe, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    print __name__
    while(True):
      retcode = p.poll() #returns None while subprocess is running
      line = p.stdout.readline()
      yield line
      if(retcode is not None):
        break

print __name__
for line in runProcess('scp ./test2.py jonathon@jljfoto2:/tmp/test2.py'.split()):
    print line

#p = subprocess.Popen(['scp', './test2.py', 'jonathon@jljfoto:/tmp/test2.py'], stdout=subprocess.PIPE,stderr=subprocess.PIPE)
#while(True):
#    retcode = p.poll() #returns None while subprocess is running
#    line = p.stdout.readline()
#    yield line
#    if(retcode is not None):
#      break

#out, err = p.communicate()
#print out
