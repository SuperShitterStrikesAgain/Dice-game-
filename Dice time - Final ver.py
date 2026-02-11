import random
def initpoints(whichplayer):
    double = "no"

    roll_one = random.randint(1, 6)
    roll_two = random.randint(1, 6)

    if roll_one == roll_two:
        double = "yes"

    total = roll_one + roll_two

    print(f"{whichplayer}| Roll 1: {roll_one}| Roll 2: {roll_two}| Total: {total}")
    return total, double


def instructions():


    print("go gamblingy ")

def y_n(question):
    while True:

        response = input(question).lower()

        if response == "yes" or response == "y":
            print("This is a luck based game. If you roll a 13, you win, and vice versa.")
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("Give me an yes or no answer.")
def intcheck():
    error = "please enter a number less than/equal to 13."

    while True:
        try:
            response = int(input("what is the game goal? "))

            if response < 1 or response > 13:
                print(error)
            else:
                return response


        except ValueError:
                print(error)
def makestat(state):
    ends = decor
    print (f"\n{starts} {state} {ends}")
decor = "⋆｡𖦹°⭒˚｡⋆"
starts = "⋆｡°⭒˚𖦹｡⋆"
makestat("Welcome to the game.")
y_n("Do you want to see the Instructions?")

game_goal  = int(input("Game goal: "))

com_s = 0
user_s = 0
rounds = 0

gamehistory = []

while com_s < game_goal and user_s < game_goal:

    rounds += 1

    makestat(f"Round {rounds}")
    inituser = initpoints("User")
    initcom = initpoints("Com")

    user_p = inituser[0]
    com_p = initcom[0]

    com_s += com_p
    user_s += user_p


    double_user = inituser[1]
    double_com = initcom[1]

    if double_user == "yes":
        print("If you win, Points are doubled.")

    if double_com == "yes":
        print("If I win, Points are doubled for me.")

    first = "User"
    second = "Com"
    player1p = user_p
    player2p = com_p
    user_p = 0
    com_p = 0
    if user_p > com_p:
        makestat("You start.")
    if com_p > user_p:
        makestat("I start")
        player1p, player2p = player2p, player1p
        first, second = second, first
    if user_p == com_p:
        makestat("Go ahead.")

    while player2p < 13 and player1p < 13:
        print()
        input("Press enter to continue this round\n")

        player1roll = random.randint(1, 6)
        player1p += player1roll

        print(f"{first}: Rolled a {player1p} - has {player1p} points.")

        if player1p > 13:
            break

        player2roll = random.randint(1, 6)
        player2p += player2roll

        print(f"{second}: Rolled a {player2p} - has {player2p} points.")

        print(f"{first}: {player1p} | {second}: {player2p}")

    user_p = player1p
    com_p = player2p

    if first == "Com":
        user_p, com_p = com_p, user_p

    if user_p > com_p:
        win = "User"
        com_p = 0
    else:
        win = "Com"
        user_p = 0

    feedback = f"The {win} won."

    gameres = f"Round {rounds}: User points {user_p} | Com points {com_p}, {win} wins ({user_s} | {com_s})"

    gamehistory.append(gameres)

    if win == "User" and double_user == "yes":
        user_p = user_p * 2

    if win == "Com" and double_com == "yes":
        com_p = com_p * 2

    makestat("Round Results:")
    makestat(f"User points: {user_p} | Com points: {com_p}")
    makestat(feedback)
    print()
makestat("Game Over")

if com_p > user_p:
    makestat("The computer won.")
elif user_p > com_p:
    makestat("You won.")

makestat("Game History")

for item in gamehistory:
    makestat(item)