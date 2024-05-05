import requests

res = requests.get('https://baconipsum.com/api/?type=all-meat&sentences=3')
print(res.json())
