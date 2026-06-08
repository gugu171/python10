print("Welcome to the half pyramid star maker!")
n=int(input("Enter how many rows you want in your triangle : "))
for i in range(n):
    for k in range(n - i + 1):
        print(" ", end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()
