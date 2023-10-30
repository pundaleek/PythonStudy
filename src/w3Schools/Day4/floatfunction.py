'''
float() function
This function is used to perform the following conversions.
1. float to float
2. int to float
3. string to float
4. boo to float
'''

# WAP to input 2 float values & perform addition

# n1 = float(input("Enter the number 1 : "))
# n2 = float(input("Enter the number 2 : "))
# n3 = n1 + n2
# print(n1, '\v', n2, '\v' , n3)

# n1 = int(input("Enter the number 1 : "))
# n2 = float(input("Enter the number 2 : "))
# n3 = int(n1 + n2)
# print(n1, '\v', n2, '\v' , n3)
# print(type(n1), '\t', type(n2), '\t', type(n3))

# # Write a program to swap two float numbers
# num1 = float(input("1st float number : "))
# num2 = float(input("1st float number : "))
# print("Before swap : ", num1, "\t", num2)
# num1 = num1 + num2   # 10+20=30
# num2 = num1 - num2   # 30-20=10
# num1 = num1 - num2   # 30-10=20
# print("After swap : ", num1, "\t", num2)

# Write a program to swap two numbers
num1 = 100
num2 = 200
print("Before swap : ", num1, "\t", num2)
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2
print("After swap : ", num1, "\t", num2)

# Write a program to swap two float numbers using temp or 2rd variable
a = float(input("First Float Number "))
b = float(input("Second Float Number "))
# Method1
print("Before Swaping ", a, b)
c = a
a = b
b = c
print("After Swaping ", a, b)

# Method2
a, b = b, a
print("After Swaping ", a, b)
