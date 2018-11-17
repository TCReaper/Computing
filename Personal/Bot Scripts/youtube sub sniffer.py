import json
import urllib.request
import time


# youtube sniffer


alpha = 'pewdiepie'
bravo = 'tseries'
api_key = 'AIzaSyB04qCiBaBnW-pWVz-9bidojUvZAzeJvhg'

def get_subs(name,key):
      data = urllib.request.urlopen("https://www.googleapis.com/\
youtube/v3/channels?part=statistics&forUsername="+name+"&key="+key).read()
      
      subcount = json.loads(data)["items"][0]["statistics"]["subscriberCount"]

      return subcount


temp = 0
start = str(int(get_subs(alpha,api_key))-int(get_subs(bravo,api_key)))
while True:
      
      
      alpha_subs = get_subs(alpha,api_key)
      bravo_subs = get_subs(bravo,api_key)
      
      difference = str(int(alpha_subs)-int(bravo_subs))

      change = int(difference)-int(temp)
            
      temp = difference

      print('{0} vs {1}: {2},     change: {3},\t total: {4}'.\
            format(alpha,bravo,difference,change,int(difference)-int(start)))

      
      time.sleep(5)
