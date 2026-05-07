num=int(input("Enter a number: "))
sum=0
temp=num
while temp>0:
    d=temp%10
    sum+=d**3
    temp=temp//10
    print(sum)
if sum == num:
    print("This is an armstrong number.")
else:
    print("This is NOT an armstrong number")
