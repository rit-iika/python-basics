import requests

requests.get
x = requests.get('https://w3schools.com/python/demopage.htm')

print(x.text)