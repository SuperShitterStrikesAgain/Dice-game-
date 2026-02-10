import random
def initpoints(whichplayer):
    double = "no"

    roll_one = random.randint(1, 6)
    roll_two = random.randint(1, 6)

    if roll_one == roll_two:
        double = "yes"

    total = roll_one + roll_two

    print(f"{whichplayer} Roll 1 {roll_one} Roll 2 {roll_two} Total {total}")
    return total, double
user_p = 0
com_p = 0
double_user = "no"
double_com = "no"

user_one = random.randint(1,6)
user_two = random.randint(1,6)

if user_one == user_two:
    double_user = "yes"

com_one = random.randint(1,6)
com_two = random.randint(1,6)

if com_one == com_two:
    double_com = "yes"
user_p += user_one + user_two
com_p += com_one + com_two

print("\ninitial points:")
print(f"user - Roll 1 - {user_one} Roll 2 - {user_two} total - {user_p}")
print(f"com - Roll 1 - {com_one} Roll 2 - {com_two} total - {com_p}")
if double_user == "yes":
    print("If you win, Points are doubled.")

if double_com == "yes":
    print("If I win, Points are doubled for me. If you get it, why don't i?")
