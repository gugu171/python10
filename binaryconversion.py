dnum = int(input("Enter a decimal number: "))
bstr = "" 

if dnum == 0:
    print("Binary: 0")
else:
    while dnum > 0:
        remainder = dnum % 2 
        dnum = dnum // 2
        bstr = str(remainder) + bstr 
    print("Binary:", bstr)