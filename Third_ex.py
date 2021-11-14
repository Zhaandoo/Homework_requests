import requests
from pprint import pprint


url = "https://api.stackexchange.com/2.3/questions"
headers = {'Accept': 'application/json'}
params = {'fromdate': '1636675200', 'todate': '1636848000', 'order': 'desc', 'sort': 'activity',
          'tagged': 'python', 'site': 'stackoverflow'}
response = requests.get(url, headers=headers, params=params)
pprint(response.json())
