import requests
import json

url = "https://66095c000f324a9a28832d7e.mockapi.io/users"

r = requests.get(url)

print(r.content)

r = requests.get(url)
json = r.json()

# print(json)
count_first_76 = 0
i = 0
for nam in json:
    i = i+1
    if i < 76:
        count_first_76 += float( nam['state'])

    if nam['name'] == 'Wilson VonRueden':
        print(f"Id Wilson VonRueden is: {nam['id']}")

print(f"Count for first 76 is: {count_first_76}")






# data = {'sender': 'Alice', 'receiver': 'Bob', 'message': 'We did it!'}
# data_json = json.dumps(data)
# payload = {'json_payload': data_json}
# r = requests.post(url, data=payload)