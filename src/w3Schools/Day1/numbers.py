"""
Python Numbers
There are three numeric types in Python:

int - Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
float - Float, or "floating point number" is a number, positive or negative, containing one or more decimals. Float can also be scientific numbers with an "e" to indicate the power of 10.
complex - Complex numbers are written with a "j" as the imaginary part:
Variables of numeric types are created when you assign a value to them:
"""

import random
x = 10
y = 20.587
z = 100j

# print(type(x))
# print(type(y))
# print(type(z))

x = 3+5j
y = 5j
z = -5j

# print(type(x))
# print(type(y))
# print(type(z))

"""
Type Conversion
You can convert from one type to another with the int(), float(), and complex() methods:

Note: You cannot convert complex numbers into another number type.
"""

x = 1    # int
y = 2.8  # float
z = 1j   # complex

# convert from int to float:
a = float(x)

# convert from float to int:
b = int(y)

# convert from int to complex:
c = complex(x)

print(a)  # 1.0
print(b)  # 2
print(c)  # 1+0j

print(type(a))
print(type(b))
print(type(c))

"""
Random Number

Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:
"""


print(random.randrange(1, 1000))

