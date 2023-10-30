#  Write a program to print avg input 5 numbers

num = 1
sum = 0

while num <= 5:
    input_number = int(input("Enter the number : "))
    sum = sum + input_number
    num = num + 1
average = sum / 5

print(f"Sum of numbers is {sum}")
print(f"Average of all numbers is {average:.2f}")