import requests

import json

from env import *



# print("hello")

API_KEY=os.environ["API_KEY1"]
print(API_KEY)
LOCATION="Nairobi"

# response=requests.get(f'https://samples.openweathermap.org/data/2.5/weather?q={LOCATION},KE&appid={API_KEY}')

response=requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={LOCATION},ke&appid={API_KEY}')

# print(type(data))
print(response.json())

print(type(response.json()))

def getStringJson(data):
	text=json.dumps(data,sort_keys=True,indent=4)

	# print(type(text))

	print(text)

def convertToObject(data):
	text=json.loads(data)
	print(text)


def dumpToFile(data):

	if response.status_code==200:
		with open("data.json","w",encoding='utf-8') as f:
			json.dump(data,f,ensure_ascii=False,indent=4)

	

# convertToObject(response.text())
# read from json fiel

def readFile():
	with open("data.json") as f:
		data=json.load(f)

		print(data["coord"])

dumpToFile(response.json())
# readFile()