import random
def random_num(arg2, arg3):
    arg4 = random.randint(arg2, arg3)
    return arg4
    if textperm == "True":
        print(arg4)

def text(arg):
    print(arg)

def guess_the_num():
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

def dice(leave_empty_with_commas):
    if leave_empty_with_commas == "help":
        print("it aint a game but it is something")

    computer_choice = random.randint(1, 6)
    your_choice = input("Roll the dice y/n ")
    if your_choice == "y":
        your_choice = random.randint(1, 6)
        print(f"Your dice rolled {your_choice}")
        print(f"while the computer rolled {computer_choice}")
    else:
        print("see ya")

def timer(seconds):
    start = input("Start >>> ")
    if start == "yes" or start == "Yes":
        def clear():
            import os
            os.system("clear")

        second = seconds
        while True:
            second -= 1
            print(second)
            clear()
            time.sleep(1)
            if second == 0:
                break
        print("It finished!")
