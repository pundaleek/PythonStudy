'''
eval() function
It is used t evaluate expression represented as a string()
When we don't know the type of data then should go with eval()
'''

res1=eval("5+2")
print(res1)
print(type(res1))

res2=eval("5.0+2.0")
print(res2)
print(type(res2))

res3=eval("45")
print(res3)
print(type(res3))

res4=eval("1.5")
print(res4)
print(type(res4))

res5=complex("1+2j")
print(res5)
print(type(res5))

# WAP to input 2 nums & perform addition
num1 = eval(input("Enter num1 "))
num2 = eval(input("Enter num2 "))
sum = num1 + num2
print(sum)
print(type(num1), "\t", type(num2), "\t", type(sum))