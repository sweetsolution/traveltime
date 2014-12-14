__author__ = 'suess'

import urllib.request
import json


## gogole directions API
## https://developers.google.com/maps/documentation/directions/?hl=de

## in Android
##http://stackoverflow.com/questions/20979853/getting-distance-from-google-direction-api-in-android

startpoint ="Karlsruhe"
endpoint = "Pforzheim"


URL2 = "http://maps.googleapis.com/maps/api/directions/json?origin="+startpoint+"&destination="+endpoint+"&sensor=false&mode=driving&units=metric"
googleResponse = urllib.request.urlopen(URL2);

str_response = googleResponse.readall().decode('utf-8')
data = json.loads(str_response)


erg = data['routes']
#########################print('result = ' + str(erg))

legs = data['routes'][0]['legs']
summary = data['routes'][0]['summary']

dauer = (legs[0]['duration']['text'])

print ("Travelitime " +"("+str(summary)+") = " + str(dauer))
