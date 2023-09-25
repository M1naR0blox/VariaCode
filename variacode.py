import time
import random
import os

# Print text()

def text():
    print()

# To use, put variables between

variable = 2 + 2

def text(variable):
    print(variable)

# clear()
def clear():
    os.system("clear")

# Sleep
def sleep():
    time.sleep(1)  

# Input

inpvariable = "Do you like oranges? "

def type(prompt):
    return input(prompt)

# inputvariable = type(inpvariable)

# int(input)

intinput = "How many numbers does 10 have? "

def numtype(prompt2):
    return int(input(prompt2))

# intedinput = numtype(intinput)

# if stataments = higher

answertointinput = 2

fail = "you failed the question"

def higher(intedinput, answertointinput):
    if intedinput > answertointinput:
        text(fail)

# if statements = lower

def lower(intedinput, answertointinput):
    if intedinput < answertointinput:
        text(fail)

# if statements = equal

success = "You got right the answer."

def equal(intedinput, answertointinput):
    if intedinput == answertointinput:
        text(success)        



intedinput = numtype(intinput)

lower(intedinput, answertointinput)

higher(intedinput, answertointinput)

equal(intedinput, answertointinput)

# Random = numbers

minnumber = 1
maxnumber = 100
randomresult = 0

def randomnum(minnumber, maxnumber):
    randomresult = random.randint(minnumber, maxnumber)
    print(randomresult)
randomnum(minnumber, maxnumber)
