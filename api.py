import requests 
import json
import pprint
url = 'https://api.tvmaze.com/singlesearch/shows'
show = input("Please input a show name >>")
params = {"q":show}

response = requests.get(url, params)

if response.status_code ==200:
    data = json.loads(response.text)
    #pprint.pprint(data)
    name = data ['name']
    premiered = data['premiered']
    summary = data ['summary']
    print(f"{ name} premiered on {premiered}")
    print(summary)
else:
    print(f"Error;{respose.status_code}")
