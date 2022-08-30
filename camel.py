import random
import time
import sys


def intro():  # single player introduction statement
    delay_prints("Welcome to Camel!\n")
    delay_prints(
        "You have stolen a camel to make your way across the great Mobi desert.\nThe natives want their camel back and "
        "are chasing you down!\n")
    delay_prints("Survive your desert trek and out run the natives.\n")
    delay_prints("If you're stamina reaches 3, dehydration reaches 3 or if the natives catch you, you dead\n")
    delay_prints("Good Luck Friend :)")
    time.sleep(1)
    game()


def m_intro():  # multiplayer introduction statement
    playercount = input('How many people are playing?')
    delay_prints("Welcome to Camel!\n")
    delay_prints(
        "The thief has stolen a camel to make their way across the great Mobi desert.\nThe natives want their camel back and "
        "are chasing him down!\n")
    delay_prints("Survive the desert trek and out run the natives.\n")
    delay_prints("If the thief's stamina reaches 3, dehydration reaches 3 or if the natives catch you, you dead\n")
    delay_prints("The role will rotate around the amount of players playing!\n")
    delay_prints("WARNING, GAME WORKS BETTER WITH LOWER AND EVEN AMOUNT OF PLAYERS\n")
    time.sleep(1)
    gamer(playercount)


def delay_prints(s):  # prints text character by character
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(.03)


def get_age():  # asks the user for their age, if they are under 8 or over 100 they won't be allowed to play.
    while True:
        Age = input("Please enter your age: ")
        try:
            checker = int(Age)
            if checker >= 100:
                delay_prints("Sorry 100 is the maximum age allowed")
                sys.exit()
            elif checker >= 8:
                delay_prints("You are old enough to play the game\n"
                             "Continue on traveler\n")
                time.sleep(0.75)
                multiplayer()
                break
            elif checker:
                delay_prints("Sorry you are not old enough to play this game")
                time.sleep(0.75)
                sys.exit(0)
            else:
                pass
        except ValueError:
            delay_prints("Amount must be a number, try again\n")
            time.sleep(0.75)
    return checker


def gamer(playercount):  # if there is more than two players, it uses the multiplayer code
    t_canteen = 4
    n_canteen = 4
    t_thirst = 0
    n_thirst = 0
    distanceTraveled = 0
    nativesTraveled = -20
    t_camel_stamina = 0
    n_camel_stamina = 0
    done = False
    playercount = int(playercount)
    currentplayer = 1
    x = 3  # fixes hardcoded values
    z = 1
    w = 0

    while not done:
        if currentplayer > playercount:
            currentplayer = 1

        max_speed: int = random.randrange(10, 20)
        normal_speed: int = random.randrange(4, 15)

        print("It is players " + str(currentplayer) + " turn!")
        print("""
        Thief's Turn:
        A. Drink from your canteen.
        B. Ahead at moderate speed.
        C. Ahead full speed.
        D. Stop for the night.
        E. Status check
        Q. Quit.\n """)
        # asks user what option they would like to pick
        # looks for what character they entered and shows info.
        userInput: str = input("What option would you like to pick?")

        # if user puts q, the game ends.
        if userInput.lower() == "q":
            delay_prints("later boss")
            time.sleep(0.5)
            sys.exit()

        # drink from canteen
        elif userInput.lower() == "a":
            if t_canteen == w:
                print("You're out of water.")
            else:
                t_canteen -= z
                t_thirst *= w
                print("You are no longer dehydrated, and you have ", t_canteen, " drinks left.")
            # player = "2"

        # if thirst equals 3 then the camel dies of dehydration
        elif t_thirst == x:
            print("You died of dehydration")
            again()
        # move at moderate speed
        elif userInput.lower() == "b":
            print("You traveled ", normal_speed, " miles.")
            distanceTraveled += normal_speed
            t_thirst += z
            t_camel_stamina += z
            distrav(distanceTraveled)
            thirsty(t_thirst)
            camstam(t_camel_stamina)
            # player = "2"

        # move at full speed
        elif userInput.lower() == "c":
            print(" You traveled ", max_speed, " miles.")
            distanceTraveled += max_speed
            t_thirst += z
            t_camel_stamina += random.randrange(1, 2)
            distrav(distanceTraveled)
            thirsty(t_thirst)
            camstam(t_camel_stamina)
            # player = "2"

        # stop for the night.
        elif userInput.lower() == "d":
            t_camel_stamina *= w
            print("Your camel feels refreshed and happy his fatigue is now ", t_camel_stamina)
            distrav(distanceTraveled)
            thirsty(t_thirst)
            camstam(t_camel_stamina)
            # player = "2"
            # if camel stamina is 3, then the camel will die of tiredness
        elif t_camel_stamina == x:
            print("You're camel died of tiredness")
            again()
            # game status
        elif userInput.lower() == "e":
            print("You have traveled:", distanceTraveled, "out of 100 miles required")
            time.sleep(0.75)
            print("Drinks in canteen:", t_canteen)
            time.sleep(0.75)
            print("Your camel has", t_camel_stamina, "amount of stamina.")
            time.sleep(0.75)
            print("Thirst:", t_thirst)
            time.sleep(0.75)
            print("The natives are", (distanceTraveled - nativesTraveled), "miles behind you.")
            time.sleep(1.5)
        else:
            delay_prints("Please enter a valid character :)")  # prints the error message
        currentplayer += 1
        if currentplayer > playercount:  # once the max amount of players are reached, it resets back to player 1s turn
            currentplayer = 1

        max_speed: int = random.randrange(10, 22)
        normal_speed: int = random.randrange(4, 17)
        print("It is players " + str(currentplayer) + " turn!")
        print("""
        Natives' Turn:
        A. Drink from your canteen.
        B. Ahead at moderate speed.
        C. Ahead full speed.
        D. Stop for the night.
        E. Status check
        Q. Quit.\n """)
        # asks user what option they would like to pick
        # looks for what character they entered and shows info.
        userInput: str = input("What option would you like to pick?")

        # if user puts q, the game ends.
        if userInput.lower() == "q":
            delay_prints("later boss")
            time.sleep(0.5)
            sys.exit()

        # drink from canteen
        elif userInput.lower() == "a":
            if n_canteen == w:
                print("You're out of water.")
            else:
                n_canteen -= z
                n_thirst *= w
                print("You are no longer dehydrated, and you have ", n_canteen, " drinks left.")
            caught(distanceTraveled, nativesTraveled)
            # player = "1"

        # if thirst equals 3 then the camel dies of dehydration
        elif n_thirst == x:
            print("You died of dehydration")
            again()
        # move at moderate speed
        elif userInput.lower() == "b":
            print("You traveled ", normal_speed, " miles.")
            nativesTraveled = nativesTraveled + normal_speed
            n_thirst += z
            n_camel_stamina += z
            caught(distanceTraveled, nativesTraveled)
            distrav(distanceTraveled)
            thirsty(n_thirst)
            camstam(n_camel_stamina)
            # player = "1"

        # move at full speed
        elif userInput.lower() == "c":
            print(" You traveled ", max_speed, " miles.")
            nativesTraveled = nativesTraveled + max_speed

            n_thirst += z
            n_camel_stamina += random.randrange(1, 2)
            caught(distanceTraveled, nativesTraveled)
            distrav(distanceTraveled)
            thirsty(n_thirst)
            camstam(n_camel_stamina)
            # player = "1"

        # stop for the night.
        elif userInput.lower() == "d":
            n_camel_stamina *= w
            print("Your camel feels refreshed and happy his fatigue is now ", n_camel_stamina)
            caught(distanceTraveled, nativesTraveled)
            distrav(distanceTraveled)
            thirsty(n_thirst)
            camstam(n_camel_stamina)
            # player = "1"
            # if camel stamina is 3, then the camel will die of tiredness
        elif n_camel_stamina == x:
            print("You're camel died of tiredness")
            again()
            # game status
        elif userInput.lower() == "e":
            print("The thief has traveled:", distanceTraveled, "out of 100 miles required")
            time.sleep(0.75)
            print("Drinks in canteen:", n_canteen)
            time.sleep(0.75)
            print("Your camel has", n_camel_stamina, "amount of stamina.")
            time.sleep(0.75)
            print("Thirst:", n_thirst)
            time.sleep(0.75)
            print("You are", (distanceTraveled - nativesTraveled), "miles behind the thief.")
            time.sleep(1.5)
        else:
            delay_prints("Please enter a valid character :)")  # prints the error message
        currentplayer += 1  # goes to the next players turn


def game():  # if only one player is playing, they use the single player code
    canteen = 4
    thirst = 0
    distanceTraveled = 0
    nativesTraveled = -20
    camel_stamina = 0
    done = False
    print()
    natives_distance = distanceTraveled - nativesTraveled
    x = 3
    z = 1
    w = 0

    while not done:

        max_speed: int = random.randrange(10, 20)
        normal_speed: int = random.randrange(4, 15)

        # if camel stamina is 3, then the camel will die of tiredness
        if camel_stamina == x:
            print("You're camel died of tiredness")
            again()
            # if thirst equals 3 then the camel dies of dehydration
        if thirst == x:
            print("You died of dehydration")
            again()

        print("""
        A. Drink from your canteen.
        B. Ahead at moderate speed.
        C. Ahead full speed.
        D. Stop for the night.
        E. Status check
        Q. Quit.\n """)
        # asks user what option they would like to pick
        # looks for what character they entered and shows info.
        userInput: str = input("What option would you like to pick?")

        # if user puts q, the game ends.
        if userInput.lower() == "q":
            delay_prints("later boss")
            time.sleep(0.5)
            done = True

        # drink from canteen
        elif userInput.lower() == "a":
            if canteen == w:
                print("You're out of water.")
            else:
                canteen -= z
                thirst *= w
                print("You are no longer dehydrated, and you have ", canteen, " drinks left.")
                caught(distanceTraveled, nativesTraveled)

        # move at moderate speed
        elif userInput.lower() == "b":
            print("You traveled ", normal_speed, " miles.")
            distanceTraveled += normal_speed
            thirst += z
            camel_stamina += z
            nativesTraveled += random.randrange(5, 16)
            caught(distanceTraveled, nativesTraveled)
            distrav(distanceTraveled)
            thirsty(thirst)
            camstam(camel_stamina)
            gaining(natives_distance)
        # move at full speed
        elif userInput.lower() == "c":
            print(" You traveled ", max_speed, " miles.")
            distanceTraveled += max_speed
            thirst += z
            camel_stamina += random.randrange(1, 2)
            nativesTraveled += random.randrange(5, 16)
            caught(distanceTraveled, nativesTraveled)
            distrav(distanceTraveled)
            thirsty(thirst)
            camstam(camel_stamina)
            gaining(natives_distance)
        # stop for the night.
        elif userInput.lower() == "d":
            camel_stamina *= w
            print("Your camel feels refreshed and happy his fatigue is now ", camel_stamina)
            nativesTraveled += random.randrange(5, 16)
            caught(distanceTraveled, nativesTraveled)
            distrav(distanceTraveled)
            thirsty(thirst)
            camstam(camel_stamina)
            gaining(natives_distance)

        # game status
        elif userInput.lower() == "e":
            print("You have traveled:", distanceTraveled, "out of 100 miles required")
            time.sleep(0.75)
            print("Drinks in canteen:", canteen)
            time.sleep(0.75)
            print("Your camel has", camel_stamina, "amount of stamina.")
            time.sleep(0.75)
            print("Thirst:", thirst)
            time.sleep(0.75)
            print("The natives are", (distanceTraveled - nativesTraveled), "miles behind you.")
            time.sleep(1.5)
        # if the user inputs a character that isn't recognized, an error message will be printed
        else:
            delay_prints("Please enter a valid character :)")  # prints the error message


def distrav(x):  # code for winning the game
    if x >= 100:
        delay_prints("You escaped the natives!\n")
        again()


def thirsty(x):  # code for letting the user know they are thirsty
    if x >= 2:
        delay_prints("You are thirsty, drink water!\n")
        time.sleep(0.75)


def camstam(x):  # code for letting the user know the camel is tired
    if x >= 2:
        delay_prints("Your camel is tired, sleep up!\n")
        time.sleep(0.75)


def gaining(x):  # code for telling the user that the natives are gaining on them
    if x <= -0:
        delay_prints("The natives are gaining on you!")


# checks if distanceTravelled is less than the Natives, meaning we've been caught
def caught(x, y):
    if x <= y:
        print("The natives caught you!")
        again()

    else:
        print("You're not dead yet!")
        time.sleep(1.5)


def m_caught(x, y):  # checks if distanceTravelled is less than the Natives, meaning the thief has been caught
    if x <= y:
        print("The thief is caught! Get rekt")
        again()
    else:
        print("The thief is on the loose!")
        time.sleep(1.5)


# game()
# asks the user if they would like to play multiplayer
def multiplayer():
    while True:
        # str.lower used to turn cap Y/N into lowercase so doesnt matter what the user puts
        choice = str.lower(str(input('Would you like to play multiplayer? Y/N')))
        if choice == 'y':
            m_intro()
            break
        elif choice == 'n':
            intro()
            break
        else:
            print('Invalid option')


def again():  # asks if the user wants to play again, if they say yes it runs the game again, if they say no it exits
    play_again = str(input("Do you want to play again (type yes or no): "))
    if play_again == "yes":
        multiplayer()

    elif play_again == "no":
        delay_prints("later boss")
        time.sleep(0.75)
        sys.exit()

    else:
        delay_prints("Please enter a valid character :)")  # prints the error message


get_age()
