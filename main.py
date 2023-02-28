import random

for i in range(3):

    with open("names.txt", "r") as file:
        name_list = [line.strip() for line in file.readlines()]

    left_hero = random.choice(name_list)
    name_list.remove(left_hero)
    right_hero = random.choice(name_list)

    user_okay = True
    with open("choices.txt", "a") as choices_file:
        while user_okay:
            user_choice = input(f"Tapez 1 si vous votez pour {left_hero}, ou 2 si vous votez pour {right_hero}.")
            if user_choice == "1":
                print(f"Vous avez voté pour {left_hero} !")
                choices_file.write(left_hero + "\n")
                user_okay = False
            elif user_choice == "2":
                print(f"Vous avez voté pour {right_hero} !")
                choices_file.write(right_hero + "\n")
                user_okay = False
            else:
                print("Merci de taper uniquement 1 ou 2, espèce de gros naze.")
                user_okay = True

score = {}

with open("choices.txt", "r") as choices_file:
    for line in choices_file:
        name = line.strip()
        if name in score:
            score[name] += 1
        else:
            score[name] = 1

print(score)