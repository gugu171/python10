l=int(input("Enter your lower range: "))
u=int(input("Enter you upper range: "))
for i in range(l,u+1):
    if i>1:
        for j in range(2,i):
            if i%j == 0:
                break
        else:
            print(i,end=(" "))