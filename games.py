import random
def random_num(arg2, arg3):
    arg4 = random.randint(arg2, arg3)
    return arg4
    if textperm == "True":
        print(arg4)

def text(arg):
    print(arg)

def games(option):
    if option == "":
        text("To choose a game, please put in on the code")

    if option == "help":
        text("Type the name, not the number")
        text("1.- Guess the number")
        text("2.- Coming soon")

    if option == "Guess the number":
        randomnumber = random_num(1, 100000)
        text("Guess the number")
        while True:
            playernumber = int(input(">>> "))
            if playernumber > randomnumber:
                text("You Passed It")
            if playernumber < randomnumber:
                text("You Havent Passed It")
            if playernumber == randomnumber:
                text("You Won!")
            if playernumber == "break":
                break


    else:
        text("This game aint existing")

games("Guess the number")