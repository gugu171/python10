print("Random ASCII Checker")
c=input("Enter a SINGLE character: ")
if type(c) is str and len(c) == 1:
    print("Good! You entered a single character.")
else:
    print("I SAID ENTER A SINGLE CHARACTER!\nBAD ENDING")
ascii_val = ord(c)
print("Character: ",c)
print("ASCII value:",ascii_val)
if ascii_val >=65 and ascii_val <=90:
    print("This is an uppercase letter")
elif ascii_val >=97 and ascii_val <=122:
    print("This is a lowercase letter")
elif ascii_val >=48 and ascii_val <=57:
    print("This is a number")
elif ascii_val ==32:
    print("You have entered space")
else:
    print("You have entered a special character")
print("now you know what ascii number your character is!")
