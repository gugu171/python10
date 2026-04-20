m=int(input("Enter your maths marks from 1-100: "))
e=int(input("Enter your english marks from 1-100: "))
s=int(input("Enter your science marks from 1-100: "))
c=int(input("Enter your computing marks from 1-100: "))
t=m+e+s+c
p=(t/400)*100
if p>=95:
    print("You got A*")
elif p>=91:
    print("You got an A")
elif p>=82:
    print("You got a B") 
elif p>=78:
    print("You got a C")
elif p>=74:
    print("You got a D")
else:
    print("You have an F")



