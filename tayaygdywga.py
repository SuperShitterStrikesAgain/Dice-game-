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

def makestat(state):
    ends = decor
    print (f"\n{starts} {state} {ends}")
decor = "⋆｡𖦹°⭒˚｡⋆"
starts = "⋆｡°⭒˚𖦹｡⋆"



game_goal  = int(input("Game goal: "))



while com_p < game_goal and user_p < game_goal:
    
    inituser = initpoints("User")
    initcom = initpoints("Com")

    user_p = inituser[0]
    com_p = initcom[0]

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
    else:
        win = "Com"

    feedback = f"The {win} won."

    if win == "User" and double_user == "yes":
        user_p = user_p * 2

    if win == "Com" and double_com == "yes":
        com_p = com_p * 2

    makestat("Round Results:")
    makestat(f"User points: {user_p} | Com points: {com_p}")
    makestat(feedback)
    print()