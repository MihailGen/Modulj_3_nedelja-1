import requests
import datetime

url = "https://66095c000f324a9a28832d7e.mockapi.io/users"
r = requests.get(url)
count_first_76 = 0
i = 0
oldest_birth = "2024-04-21T11:44:06.223Z"
state = 0
birth_in_april = 0

for user in r.json():
    i += 1
    if i == 1:
        min_state = float(user['state'])
    # общее состояние первых 76 пользователей
    if i < 76:
        count_first_76 += float(user['state'])

    # кто самый пожилой
    if user['birth'] < oldest_birth:
        oldest = user['birth']
        name_oldest = user['name']

    # сколько родилось в апреле
    if user['birth'][5:7] == "04":
        birth_in_april += 1

    # кто самый бедный
    if float(user['state']) < min_state:
        min_state = float(user['state'])
        name_poorest = user['name']

    # ID Wilson VonRueden
    if ['name'] == 'Wilson VonRueden':
        print(f"Id Wilson VonRueden is: {['id']}")

print(f"Count for first 76 is: {count_first_76}")
print(f"Oldest is: {name_oldest}, he(she) was born on {oldest}")
print(f"Poorest is: {name_poorest}, he(she) hav only {min_state}")
print(f"In april birth: {birth_in_april} users")

datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')

my_data = {
    "createdAt": "2024-07-23T17:29:29.564Z",
    "name": "Mihail Genzik",
    "avatar": "https://avatar.fandom.com/wiki/Fire_Nation_Man?file=Fire_Nation_Man.png",
    "state": "9_999_999_999_999",
    "birth": "1970-04-21T11:44:06.223Z",
    "id": "77"
}