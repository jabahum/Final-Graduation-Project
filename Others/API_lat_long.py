from httplib import HTTPSConnection
import json
import os
 
apiKey = "mgnlocnn1mzs2gariim4"
 
data = {
	"radioType": "gsm",
	"cellTowers": [{
		"mobileCountryCode": 724,
		"mobileNetworkCode": 5,
		"locationAreaCode": 4261,
		"cellId": 12831
	}]
}
headers = { "Content-Type" : "text/json" }
conn = HTTPSConnection("cps.combain.com",443)
conn.request("POST", "/?key="+apiKey, json.dumps(data), headers)
response = conn.getresponse()
result = json.load(response)
 
if ("location" in result):
	os.system("clear")
	print("Returned location\n\nlat:"+str(result['location']['lat'])+"\nlong:"+str(result['location']['lng']))
else:
	print("The following error occurred: "+result['error']['message'])
