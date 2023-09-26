'''
Boolean Values
In programming you often need to know if an expression is True or False.

You can evaluate any expression in Python, and get one of two answers, True or False.

When you compare two values, the expression is evaluated and Python returns the Boolean answer:
'''


def num_test(num):

    if num >= 18:
        print("Eligible for voting")

    else:
        print("Not eligible")


num_test(18000)


def find_greater_num(num1, num2, num3):

    if num1 > num2 :
        print(num1, " is greater")

    elif num2 > num3:
        print(num2, " is greater")

    else:
        print(num3, " is greater")

find_greater_num(10, 20, 30)