"""Install requests . Write 5 lines of code that fetch
https://api.github.com/users/torvalds and print the response JSON"""


import requests
response = requests.get("https://api.github.com/users/torvalds")
data = response.json()
print(data)