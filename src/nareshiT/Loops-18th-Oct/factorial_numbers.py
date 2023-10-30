num = 1
fact = 1

input_number = int(input("Enter the number : "))

while num <= input_number:
    fact = fact * num
    num = num + 1

print(fact)