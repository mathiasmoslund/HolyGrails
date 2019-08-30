import requests
from bs4 import BeautifulSoup
import random
import json
import time
sess = requests.Session()
adapter = requests.adapters.HTTPAdapter(max_retries = 20)
sess.mount('http://', adapter)

#pause i antal sekunder
pause = (0.4)


num = 1


#sorger for at scriptet looper

while 1 == 1:

 
    start = 1656478
    #vaelger account ID

    value = start - num
    num += 1

    #gor account valgt til en string
    userID = str(value)

    #finder url
    URL = 'https://tradono.com/p/'+str(userID)

    print(num)
    print(value)
    print("__________________________")


    #headers husk authorization
    headers = {
        'Host': 'api.tradono.com',
        'Connection': 'keep-alive',
        'Sec-Fetch-Mode': 'cors',
        'tradono-app-version': '1.2.139-53-g59d7aa5',
        'authorization': 'e5a64398-cc4c-4839-850e-c597326f67aa',
        'tradono-platform': 'web',
        'tradono-language': 'en',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
        'Accept': '*/*',
        'Origin': 'https://tradono.com',
        'Sec-Fetch-Site': 'same-site',
        'Referer': 'https://tradono.com/p/486620',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-GB,en;q=0.9,da-DK;q=0.8,da;q=0.7,de-DE;q=0.6,de;q=0.5,en-US;q=0.4',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '0',
    }

    #sender post request til server

  
    r = sess.post('https://api.tradono.com/users/486630/follows/'+str(value), headers=headers)
     

    #sorger for der er pause mellem hvert loop
    #ime.sleep(pause)
