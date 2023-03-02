import random
import json

with open("names.txt", "r") as file:
    name_list = [line.strip() for line in file.readlines()]

name_dict = {name: 0 for name in name_list}

names_json = json.dumps(name_dict)
with open("names_json.json", "w") as f:
    f.write(names_json)

for i in range(3):

    left_hero = random.choice(name_list)
    name_list.remove(left_hero)
    right_hero = random.choice(name_list)

    user_okay = True
    while user_okay:
        user_choice = input(f"Tapez 1 si vous votez pour {left_hero}, ou 2 si vous votez pour {right_hero}. ")
        if user_choice == "1":
            print(f"Vous avez voté pour {left_hero} !")
            with open("names_json.json", "r+") as names_json:
                data = json.load(names_json)
                data[left_hero] += 1
                names_json.seek(0)
                names_json.truncate(0)
                json.dump(data, names_json)
            user_okay = False
        elif user_choice == "2":
            print(f"Vous avez voté pour {right_hero} !")
            with open("names_json.json", "r+") as names_json:
                data = json.load(names_json)
                data[right_hero] += 1
                names_json.seek(0)
                names_json.truncate(0)
                json.dump(data, names_json)
            user_okay = False
        else:
            print("Merci de taper uniquement 1 ou 2.")
            user_okay = True

with open("names_json.json", "r") as names_json:
    data = json.load(names_json)
    print(data)
