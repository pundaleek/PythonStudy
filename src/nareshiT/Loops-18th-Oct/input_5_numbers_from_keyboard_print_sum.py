# Write a program to input 5 numbers from keyboard and print sum

num = 1
sum = 0

while num <= 10:
    input_number = int(input("Enter the number : "))
    sum = sum + input_number
    num = num + 1

print(sum)
