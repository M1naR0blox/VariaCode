import time
import random
import os

textperm = "False"


# VariaCode related thing

def text(arg):
    print(arg)


def sleep(arg1):
    time.sleep(arg1)


def clear():
    os.system("clear")


def random_num(arg2, arg3):
    arg4 = random.randint(arg2, arg3)
    return arg4
    if textperm == "True":
        print(arg4)


def random_letter(arg5, arg6):
    arg7 = random.randint(arg5, arg6)
    if textperm == "True":
        print(arg7)


def userprompt(prompt):
    usarp = input(prompt)
    if textperm == "True":
        print(usarp)


def numbprompt(prompt):
    usar = int(input(prompt))
    if textperm == "True":
        print(usar)


def higher(num1, num2):
    if num1 > num2:
        # Change code
        something = 0


def less(num3, num4):
    if num3 < num4:
        # Change code
        something = 0


def equ4l(num5, num6):
    if num5 == num6:
        # Change code
        while True:
            if num5 == num6:
                break


def equal(num5, num6):
    if num5 == num6:
        # Change code
        something = 0


def sum(sum1, sum2):
    sum3 = sum1 + sum2
    if textperm == "True":
        print(sum3)


def less(less1, less2):
    less3 = less1 - less2
    if textperm == "True":
        print(less3)


def multiply(multiply1, multiply2):
    multiply3 = multiply1 * multiply2
    if textperm == "True":
        print(multiply3)


def divide(divide1, divide2):
    divide3 = divide1 / divide2
    if textperm == "True":
        print(divide3)


def loading_anim():
    clear()
    print("Loading")
    sleep(0.2)
    clear()
    print("Loading.")
    sleep(0.2)
    clear()
    print("Loading..")
    sleep(0.2)
    clear()
    print("Loading...")
    sleep(0.2)
    clear()
    print("Loading")
    sleep(0.2)
    clear()
    print("Loading.")
    sleep(0.2)
    clear()
    print("Loading..")
    sleep(0.2)
    clear()
    print("Loading...")
    sleep(0.2)
    clear()


def calculator():
    loading_anim()
    print("Calculator by VariaCode")
    sleep(0.5)
    print("[1] Sum")
    sleep(0.5)
    print("[2] Less")
    sleep(0.5)
    print("[3] Multiply")
    sleep(0.5)
    print("[4] Divide")
    sleep(0.5)
    option = int(input(">>> "))
    while True:
        if option == 1:
            textperm = True
            u = int(input("Input first number "))
            i = int(input("Input second number "))
            sum(u, i)
            textperm = False
        if option == 2:
            textperm = True
            u = int(input("Input first number "))
            i = int(input("Input second number "))
            less(u, i)
            textperm = False
        if option == 3:
            textperm = True
            u = int(input("Input first number "))
            i = int(input("Input second number "))
            multiply(u, i)
            textperm = False
        if option == 3:
            textperm = True
            u = int(input("Input first number "))
            i = int(input("Input second number "))
            divide(u, i)
            textperm = False
        if option == 69 or option == 420 or option > 7 or option < 68:
            break


def leave():
    exit()


def windowsonly_startfile(arg1):
    os.startfile(arg1)

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
