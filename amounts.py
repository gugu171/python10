amount=int(input("Enter your amount = "))
n1=amount//50
n2=(amount%50)//20
n3=((amount%50)%20)//10
n4=(((amount%50)%20)%10)//5
print("The £50 notes you need are = ",n1)
print("The £20 notes you need are = ",n2)
print("The £10 notes you need are = ",n3)
print("The £5 notes you need are = ",n4)