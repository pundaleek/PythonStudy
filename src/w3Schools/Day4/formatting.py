'''
Formatting Output or formatting string or string formatting

A string whcih comtains replacement fields or formatting fields is called string fomrat or format string
It is done in 3 ways
1. Old style string formatting
2. New style string formatting
3. F-string (Pythom 3.8 version)
'''
# 1. Old style string formatting is similar to "C" style
n1 = 100
n2 = 200
print("%d %d %d" % (n1, n2, n1+n2))

a = 10
print("%d %o %x" % (a, a, a))

b = 1.5e3
print("%e %f " % (b, b))

c = 1.5e3
print("%e %.2f " % (c, c))

# 2. New Style Formatting
# this is using format() function
# New style string formatting allows alignments, width, fill charcetrs...a
# String contains replacement fields & each field is represented using {} braces.a
# Each field is replaced with value of the corresponding.a

txt1 = "My name is {fName}, I'm {age}".format(fName="Appu", age=39)
print(txt1)

txt2 = "My name is {0}, I'm {1}".format("Pundalik", 100)
print(txt2)

txt3 = "My name is {}, I'm {}".format("Pundaleek", 23)
print(txt3)

a = 10
b = 20
print("Sum of {} & {} is {}".format(a, b, a+b))
print("Sum of {x:} & {y:} is {z:}".format(x=a, y=b, z=a+b))
print("Sum of {x:d} {y:o} {z:x} {p:b}".format(x=a, y=a, z=a, p=a))
print("{x:d} {y:o} {z:x} {p:b}".format(x=a, y=b, z=a, p=a))
c=30
d=40
print("{0:d},{2:o},{1:x},{3:b}".format(a,b,c,d))
n1 = 1.5
print("{}".format(n1))
print("{x:f}".format(x=n1))

n2=1.5e2
print("{x:e}".format(x=n2))
print("{x:2f}".format(x=n2))

a=10
print("{:5d}".format(a))
b=100
print("{:5d}".format(b))
c=1000
print("{:5d}".format(c))
d=1000000
print("{:5d}".format(d))