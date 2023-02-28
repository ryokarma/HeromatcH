import random

score = 0
with open("names.txt", "r") as file:
    names = file.readlines()
    name_dict = {name.strip(): score for name in names}

random_name_1 = random.choice(list(name_dict.keys()))
name_dict.pop(random_name_1)
random_name_2 = random.choice(list(name_dict.keys()))

print(random_name_1)
print(random_name_2)
