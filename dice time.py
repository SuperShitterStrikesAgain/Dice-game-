from urllib import response


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
            print("Give me an answer, Human.")
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

want_int = y_n("Do you want to see the instructions?(yes/no).")

print("The loop is over.")

if want_int == "yes":
    instructions()

game_goal = intcheck()
print(game_goal)



