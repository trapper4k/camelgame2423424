import random

# prints the intro statement
print("Welcome to Camel!")
print(
    "You have stolen a camel to make your way across the great Mobi desert.The natives want their camel back and are chasing you down! Survive   your desert trek and out run the natives.")


def game():
    canteen = 4
    thirst = 0
    check = 0
    distanceTraveled = 0
    nativesTraveled = -10
    camel_stamina = 0
    done = False
    print()
    natives_distance = distanceTraveled - nativesTraveled
    max_speed: int = random.randrange(10, 20)
    normal_speed: int = random.randrange(4, 15)
    print("""
    A. Drink from your canteen.
    B. Ahead at moderate speed.
    C. Ahead full speed.
    D. Stop for the night.
    E. Status check
    Q. Quit.\n """)

    userInput: str = input("What option would you like to pick?")
    # if user puts q, the game ends.
    if userInput.lower() == "q":
        done = True
    # game status
    elif userInput.lower() == "e":
        print("Miles traveled: ", distanceTraveled)
        print("Drinks in canteen: ", canteen)
        print("Your camel has ", camel_stamina, "amount of stamina .")
        print("The natives are ", nativesTraveled, "miles behind you.")
    # drink from canteen
    elif userInput.lower() == "a":
        if canteen == 0:
            print("You're out of water.")
        else:
            canteen -= 1
            thirst *= 0
            print("You are no longer dehydrated, and you have ", canteen, " drinks left.")
    # move at moderate speed
    elif userInput.lower() == "b":
        print("You traveled ", normal_speed, " miles.")
        distanceTraveled += normal_speed
        thirst += 1
        camel_stamina += 1
        nativesTraveled += random.randrange(5, 16)
        check = random.randrange(1, 23)

    # move at full speed
    elif userInput.lower() == "c":
        print(" You traveled ", max_speed, " miles.")
        distanceTraveled += max_speed
        thirst += 1
        camel_stamina += random.randrange(1, 3)
        nativesTraveled += random.randrange(5, 16)
        check = random.randrange(1, 23)

    elif userInput.lower() == "d":
        camel_stamina *= 0
        print("Your camel feels refreshed and happy his fatigue is now ", camel_stamina)
        nativesTraveled += random.randrange(5, 16)

    else:
        print("Please enter a valid character :)")  # prints the error message


game()
