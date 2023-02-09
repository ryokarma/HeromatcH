test = True
while test:

    with open("names.txt", "r") as file:
        name_list = file.read().split()

    import random

    random_name_1 = random.choice(name_list)
    name_list.remove(random_name_1)
    random_name_2 = random.choice(name_list)



    left_hero = random_name_1
    left_wins = 0
    left_loses = 0

    right_hero = random_name_2
    right_wins = 0
    right_loses = 0

    user_okay = True
    while user_okay:
        user_choice = input(f"Tapez 1 si vous votez pour {left_hero}, ou 2 si vous votez pour {right_hero}.")
        if user_choice == "1":
            left_wins += 1
            right_loses += 1
            print(f"Vous avez voté pour {left_hero} !")
            user_okay = False
        elif user_choice == "2":
            right_wins += 1
            left_loses += 1
            print(f"Vous avez voté pour {right_hero} !")
            user_okay = False
        else:
            print("Merci de taper uniquement 1 ou 2, espèce de gros naze.")
            user_okay = True



