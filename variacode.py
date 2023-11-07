import time
import random
import os
import games
import calc

global textperm
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

def leave():
    exit()


def windowsonly_startfile(arg1):
    os.startfile(arg1)

def kind(str):
    helper = type(str)
    print(f"It is a {helper}")

def lenght(str):
    helper = len(str)
    if helper == 1:
        print(f"It has {helper} character")
    elif helper > 1:
        print(f"It has {helper} characters")
    else:
        print("it has none :v")

def first_cap(variable):
    helper = variable.capitalize()
    print(helper)

def round_nums(num, num1):
    num3 = round(num, num1)
    print(num3)
