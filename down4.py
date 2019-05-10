# importing the requests library
import requests
import json
from requests.auth import HTTPBasicAuth
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
import urllib.parse
import sys,os
# api-endpoint
def downer(bottle,numb):
    URL = "https://poly.googleapis.com/v1/assets"
#bottle='glass'
    art='art'
    API_KEY='AIzaSyA9OzLO9SdGSpoTFMyvHRF-csagjRfSVmc'
    OBJ='OBJ'
    PARAMS = {'keywords':bottle,'key':API_KEY}



    r = requests.get(url = URL, params = PARAMS)

    # extracting data in json format
    data = r.json()
    listofurls=[]
    list2ofmtl=[]
    #print(data)
    for p in data["assets"]:
        listofurls.append(p["formats"][0]['root']['url'])
      #  if p["formats"][0]['resources'][0]['url'] is not None:
      #      list2ofmtl.append(p["formats"][0]['resources'][0]['url'])
    print(listofurls)
        #for p in data['assets']:
        #    x=p['formats']
        #    for z in x:
        #        yama=z['root']
        #        lightyagami=yama['url']
        #        listofurls.append(lightyagami)
    for arth in range(0,int(numb)):
        url = listofurls[arth]
    #    if list2ofmtl[arth] is not None:
    #        urlmtl=list2ofmtl[arth]
     #       r2=requests.get(urlmtl)
      #         f.write(r.content)
        r = requests.get(url)
        with open('download/myfile%d.obj' %arth, 'wb') as f:
            f.write(r.content)
        
    return "done"
