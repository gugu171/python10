print("Welcome to the age checker! This will tell you if you are between 10-20 years of age!")
import datetime

cyear = datetime.date.today().year
byear = int(input("What year were you born? :  "))

age = cyear - byear
print("Your calculated age is:", age) 

if age >=10:
    if age <=20:
        print("Your age is either 10 or 20, or is between 10 and 20!")
    else:
        print("You are older than 20")
else:
    print("You are younger than 10.")

