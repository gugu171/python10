s1=int(input("Enter speed 1 : "))
s2=int(input("Enter speed 2 : "))
s3=int(input("Enter speed 3 : "))
t=s1+s2+s3
avg=t/3
print("The average speed is",avg)
if avg>s1 and avg>s2 and avg>s3:
    print("The average speed is greater")
elif s1>s2 and s1>s3 and s1>avg:
    print("Speed 1 is greater")
elif s2>s1 and s2>s3 and s2>avg:
    print("Speed 2 is greater")
elif s3>s2 and s3>s1 and s3>avg:
    print("Speed 3 is greater")
else:
    print("All speeds are equal")
    