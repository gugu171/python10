ac=int(input("Enter the ACTUAL COST: £"))
sc=int(input("Enter the SELLING COST: £"))

if sc>ac:
    p=sc-ac
    print("The profit you made =£",p)
else:
    l=ac-sc
    print("The loss you made =£",l)