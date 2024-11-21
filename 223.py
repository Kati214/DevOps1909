import requests

response = requests.get('http://127.0.0.1:5000/names')
result = response.json()
# print(response.json())
expected = "Alice"
actual = result[0]["name"]
assert actual == expected
# print(response.text)