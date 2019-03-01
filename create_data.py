from datetime import timedelta, date, datetime
import random
import string
import requests
import json
import os




start_date = datetime(2019, 2, 1) 

outfile = open("data.json", "w+")

try:
    lastDateOutfile = open("startingDate", "r")
    savedStartDateStr = lastDateOutfile.read()
    print savedStartDateStr
    if savedStartDateStr:
        start_date = datetime.strptime(savedStartDateStr, "%Y-%m-%d %H:%M:%S") + timedelta(minutes=1)
except Exception as e:
    print(e)

for x in range(1440*1):


    single_date = start_date + timedelta(minutes=x)
    #print ( single_date.isoformat())

    dt = single_date.strftime("%Y-%m-%d")
    
    #print ( dt)
    
#    url = "https://elastic:j8J6xNdrujtr560tUhPpJIPh@48bc81b663c64e919e8045ccb4bcbd4d.us-west1.gcp.cloud.es.io:9243/{}-fake/fake".format(dt)
    
    #print url
    
    doc = { "user" : "tutran.com", 
            "post_date" : single_date.isoformat(),  
            "message" : ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(12)) , 
            "x": x,
            "cpu": random.randint(0,100),
            "io": random.randint(0,100)
            
    }
    
    json.dump(doc, outfile)
    outfile.write("\n")

    
    print json.dumps(doc)
lastDateOutfile = open("startingDate", "w")
lastDateOutfile.write(single_date.strftime("%Y-%m-%d %H:%M:%S"));
