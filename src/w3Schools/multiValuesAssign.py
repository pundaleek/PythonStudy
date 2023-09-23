# Python Variables - Assign Multiple Values
# Many Values to Multiple Variables
x, y, z = "PH", "VJ", "KB"
print(x, y, z)

# p, q, r = "PH", "VJ"
# print(p, q)

# One Value to Multiple Variables
a = b = c = "Bijapur"
print(a)
print(b)
print(c)

# Unpack a Collection - If we have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
fruits = ["apple", "orange", "banana"]
p, q, r = fruits
print(p)
print(q)
print(r)

names = ["ph", "vj", "kb"]
n1, n2 = names
print(n1)
print(n2)