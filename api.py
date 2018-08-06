import serial
import datetime  
import time  
import sys
import urllib, urllib2
from urllib2 import Request, urlopen, URLError, HTTPError
#import urllib2
import json
import ssl 
import os, sys
 
def getVal(url):
  
        baudrate = 9600  
        portaddr = "/dev/ttyACM0"  
          
        #Headers  
        req_headers = {'Content-Type': 'application/json'}  
          
          
        # test Web API connection using simple GET  
        #url = 'https://cb-oakpi4-vis.dev.osisoft.int/piwebapi/'
        #url = 'https://pikfrank.osisoft.int/piwebapi/'

	context = ssl._create_unverified_context()
	print("before open")
	username = 'bbui'
	password = 'Asdfqwerty123'


	# use the opener to fetch a URL
	
	# Install the opener.
	# Now all calls to urllib.request.urlopen use our opener.


#	request = urllib2.Request(url)
#	base64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')

#	os.system('sh ~/Desktop/retrogamesoriginal/pass.sh&')
	request = urllib.urlopen(url, context=context)
	

#	request.add_header("Authorization", "Basic %s" % base64string)   
        
#	request = urllib2.Request(url, headers=req_headers)  
#	password_manager.add_password(None,url,'bbui','Asdfqwerty123')  

	password_manager = urllib2.HTTPPasswordMgrWithDefaultRealm()
        #password_manager = urllib2.HTTPBasicAuthHandler()  
#        password_manager.add_password(None,url,'bbui','Asdfqwerty123')  
          
        auth = urllib2.HTTPBasicAuthHandler(password_manager)  
        opener = urllib2.build_opener(auth)  
        urllib2.install_opener(opener)  
          
        try:  
                responce=request.read()
                #responce = str(responce)
                #responce = (responce[2:len(responce)-1])
                val = responce.decode("utf-8")
                val = json.loads(val)
                return val['Value']
                #print ('Responce: ', responce)  
        except  HTTPError as e:  
                print ('Error: ', e.code  )
        except  URLError as e:  
                print ('Reason: ', e.reason  )
          
val = (getVal('https://cb-oakpi4-vis.dev.osisoft.int/piwebapi/streams/F1AbEXkS_2HFm7kCzmNswAI5qJQAm3Vup2O6BGRRQAd3LcnsgXIrtHx1BS0m5Elh8VOwyuwQ0ItT0FLUEk0LUFGMVxGQUNJTElUSUVTIC0gMTYwMCBBTFZBUkFET19URVNUXENCLU9BS1BJNC1SRUxBWVxTTFRDXFdFQVRIRVJcQ0FMQ1VMQVRJT05TfE9VVFNJREUgQUlSIFRFTVBFUkFUVVJF/value'))
print(val)


'''
#URL for POST command to write a value to an AF Attribute with PI point reference  
url = 'https://<server_name>/piwebapi/streams/<WebId>/value'  
request = urllib2.Request(url, headers=req_headers)  
  
# define serial port and read temperature value.  
ser = serial.Serial(portaddr,baudrate)  
# read and skip first line of data which is usually not complete  
tempValue=ser.readline()   
  
  
while 1:  
        ts = time.time()  
        st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')  
        tempValue=ser.readline()  
        print(st + "," + tempValue)  
        #This data string works as well and PI will provide the timestamp  
        #req_data = str({"Value": x})  
          
        # use the generated timestamp from the raspPI  
        # package the request  
        req_data = str({"Timestamp": st, "Value":tempValue})  
        request = urllib2.Request(url, headers=req_headers)  
        request.add_data(req_data)  
  
        # Use try/catch to get telemetry on errors  
        try:  
                responce=urllib2.urlopen(request).read()  
        except  HTTPError as e:  
                print 'Error: ', e.code  
        except  URLError as e:  
                print 'Reason: ', e.reason  
  
  
        #Arduino sends data approx every 3 seconds.  
        time.sleep(3)  
          
        # flush serial cache or data will lag the timestamp.  
        ser.flush()  
        ser.flushInput()  
        ser.flushOutput()  
  
ser.close
'''
