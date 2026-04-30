m=input("Do you have medical? Y/N : ")
a=int(input("What is your attendance? : "))
if m=='Y':
    print("You are allowed to sit in the exam")
else:
    if a>=86:
        print("You are allowed")
    else:
        print("You are not allowed")
    

    