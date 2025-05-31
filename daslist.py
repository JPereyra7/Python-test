thisList = ["BMW", "Volvo", "Ford", "Fiat"]
thisList.insert(1, "Tesla")


def cars():
    whatcar = input("What car brand do you own? ")

    if whatcar in thisList:
        print("You have a good taste! 🚗")
    else:
        print("You own another type of car! 🚗")


cars()

