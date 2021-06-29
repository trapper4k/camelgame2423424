# create a constant to hold the threshhold of winning
THRESHHOLD_OF_LIFE_AND_DEATH = 50
def gold_room():
    print("This room is full of gold!")
    answer = input("How much gold do you take?")
    while(answer != ""):
        try:

            if (int(answer) < THRESHHOLD_OF_LIFE_AND_DEATH):
                print("Nice. You are not greedy. Take some more!")
                #break
                return answer
            else:
                print("You greedy snort! How dare you! Now you die!")
                deadly_moon()  # call the deadly_moon function here!!
                return answer     # return a value from your function!!!
        except ValueError:
            print("Enter a number you fool!")
            answer = input("Please try again!")


def bear_room():
    pass

def deadly_moon():
    print("Now you are in trouble!")

# call the gold room and start the game
#gold_room()
print(gold_room()) # do something with the returned value!!
