global textperm
textperm = "True"

def sleep(arg):
    import time
    time.sleep(arg)

def clear():
    import os
    os.system("cls")

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

calculator()