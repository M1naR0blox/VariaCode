import time
import random
import os


# Print text()

def text():
    print()

# To use, put variables betweeN

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



### intedinput = numtype(intinput)

### lower(intedinput, answertointinput)

### higher(intedinput, answertointinput)

### equal(intedinput, answertointinput)

# Random = numbers

minnumber = 1
maxnumber = 100
randomresult = 0

def randomnum(minnumber, maxnumber):
    randomresult = random.randint(minnumber, maxnumber)
    print(randomresult)

# Sum
textperm = "True"
sum1 = 2
sum2 = 2
def sum(sum1, sum2):
    sum3 = sum1 + sum2
    if textperm == "True":
        print(sum3)

# Less
rest1 = 5
rest2 = 3
def rest(rest1, rest2):
    rest3 = rest1 - rest2
    if textperm == "True":
        print(rest3)

# Multiply
multiply = 2
multiply2 = 69
def multiplier(multiply, multiply2):
    multiply3 = multiply * multiply2
    if textperm == "True":
        print(multiply3)

# Division
division1 = 50
division2 = 2
def division(division1, division2):
    division3 = division1 / division2
    if textperm == "True":
        print(division3)

# Close

def leave():
    exit()
