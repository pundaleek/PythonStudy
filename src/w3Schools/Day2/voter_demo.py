def vote_func():

    age = int(input("Enter age: "))

    if age >= 18:
        print("Candidate age is : ", age, " & is ELIGIBLE to vote")

    else:
        print("Candidate age is : ", age, " & is NOT ELIGIBLE to vote")


vote_func()