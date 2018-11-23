
import urllib.request
req = urllib.request.Request(
    #input('url: '),
    url='https://images.google.com/searchbyimage?image_url=https://cdn.discordapp.com/attachments/515083749000478730/515203927814176768/PokecordSpawn.jpg',
    data=None, 
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
)

r = urllib.request.urlopen(req)
text = r.read().decode('utf-8')

file = open('search.txt','w')
text2 = text.encode('utf-8')
file.write(str(text2))
file.close()

index = text.index('https://bulbapedia.bulbagarden.net/wiki/')
identity = text[int(index)+40:int(index)+100]
name = identity[:identity.index('_(')]
print(name)
