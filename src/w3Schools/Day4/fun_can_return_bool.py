def myFunction(text) :
  return bool(text)

print(myFunction(1))

def myFunction1() :
  return bool()

print(myFunction1())

def myFunction2() :
  return 0

if myFunction2():
  print("YES!")
else:
  print("NO!")

x = '200.1'
print(isinstance(x, str))