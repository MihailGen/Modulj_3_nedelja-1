import requests
import datetime
from pytz import timezone as tz

url = "https://66095c000f324a9a28832d7e.mockapi.io/users"
r = requests.get(url)
count_first_76 = 0
i = 0
state = 0
birth_in_april = 0

for user in r.json():
    i += 1
    try:
        birth = datetime.datetime.fromisoformat(user['birth']).replace(tzinfo=tz('UTC'))
    except:
        print(f"Incorrect birth date for ID:{user['id']}")

    if i == 1:
        min_state = float(user['state'])
        oldest_birth = datetime.datetime.fromisoformat(user['birth']).replace(tzinfo=tz('UTC'))

    # кто самый пожилой
    elif birth < oldest_birth:
        oldest_birth = birth
        # oldest = user['birth']
        name_oldest = user['name']

    # общее состояние первых 76 пользователей
    if i < 76:
        count_first_76 += float(user['state'])

    # сколько родилось в апреле
    try:
        if birth.month == 4:
            birth_in_april += 1
    except:
        print(f"Incorrect birth date for ID:{user['id']}")

    # кто самый бедный
    if float(user['state']) < min_state:
        min_state = float(user['state'])
        name_poorest = user['name']

    # ID Wilson VonRueden
    if user['name'] == 'Wilson VonRueden':
        print(f"Id Wilson VonRueden is: {user['id']}")

print(f"Count for first 76 is: {count_first_76}")
print(f"Oldest is: {name_oldest}, he(she) was born on {oldest_birth}")
print(f"Poorest is: {name_poorest}, he(she) hav only {min_state}")
print(f"In april birth: {birth_in_april} users")



my_data = {
    "createdAt": datetime.datetime.now().isoformat(),
    "name": "Mihail Genzik",
    "avatar": "https://avatar.fandom.com/wiki/Fire_Nation_Man?file=Fire_Nation_Man.png",
    "state": "9_999_999_999_999",
    "birth": "1970-04-21T11:44:06.223Z",
    "id": str(int(r.json()[len(r.json())-1]['id']) + 1)
}
print(my_data)
