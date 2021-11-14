import requests

characters = ['Hulk', 'Captain America', 'Thanos']
iq = 0
best = None
for name in characters:
    url = "https://superheroapi.com/api/2619421814940190/search/" + name
    response = requests.get(url)
    for i in response.json()['results']:
        if int(i['powerstats']['intelligence']) >= iq:
            iq = int(i['powerstats']['intelligence'])
            best = i['name']
print(f'Самый умный супергерой - {best}!')