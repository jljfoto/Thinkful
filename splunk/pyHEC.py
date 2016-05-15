"""
Sending data to Splunk's HTTP Event Collector (HEC)
Read how to setup HEC here: http://blogs.splunk.com/2015/09/22/turbo-charging-modular-inputs-with-the-hec-http-event-collector-input/
No batching (mostly because I am bored - but it is trivial to add it)
Jon V
December 07 2015
"""

import json
import requests

class PyHEC:

    def __init__(self, token, uri, port='8088'):
        if not 'http' in uri:
            raise("no http or https found in hostname")
        self.token = token
        self.uri = uri+":"+port+"/services/collector/event"
        self.port = port

    """
    event data is the actual event data
    metadata are sourcetype, index, etc
    """    
    def send(self, event, metadata=None):

	cafile = 'cacert.pem' # http://curl.haxx.se/ca/cacert.pem
        headers = {'Authorization': 'Splunk '+self.token}

        #print "type of event is: {}\n".format(type(event))
        #print "type of headers is: {}\n".format(type(headers))
        payload = event

        if metadata:
            payload.update(metadata)
            
        #print "in HEC.send..."
	#print "self.uri: |{}|".format(self.uri)
	#print "self.token: |{}|".format(self.token)
	#print "payload: |{}|".format(json.dumps(payload))
	#print "metadata: |{}|".format(metadata)
	#print "headers: |{}|".format(headers)
	#print "self.port: |{}|\n".format(self.port)

        #print "data... {}".format(json.dumps(payload))
        verify=True if 'https' in self.uri else False
        

        #print "what is sent: {} {} {} \n\n\n".format(self.uri, json.dumps(payload), headers)

        r = requests.post(self.uri, data = json.dumps(payload), headers = headers)
        #r = requests.post(self.uri, data=json.dumps(payload), headers=headers, verify=True if 'https' in self.uri else False)

        #print "status: {}".format(r.status_code)
        #print "test: |{}|".format(r.text)
        return r.status_code, r.text,
