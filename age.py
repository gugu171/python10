try:
    age_of_user=int(input("What is your age? : "))
    if age_of_user % 2 == 0:
        print("Your age is even")
    else:
        print("Your age is odd")
except SyntaxError as ex:
    print(ex)
    