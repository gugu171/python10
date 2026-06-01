rows=int(input("Enter how many rows you want in your triangle : "))
number = 1
print("Welcome to the Floyd's triangle maker!")
for i in range(1, rows+1):
    for j in range(1, i+1):
        print(number, end=(" "))
        number = number + 1
    print( )
