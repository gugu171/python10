def add(P,Q):
    return P+Q
def subtract(P,Q):
    return P-Q
def multiply(P,Q):
    return P*Q
def divide(P,Q):
    return P/Q
print("A. Add")
print("B. Subtract")
print("C. Multiply")
print("D. Divide")
choice = input("Choose one of the options using : a, b, c, and d : ")
n1 = int(input("Good. Now enter your 1st number : "))
n2 = int(input("Good. Now enter your 2nd number : "))
if choice == 'a':
    print(n1,'+',n2,'=',add(n1,n2))
elif choice == 'b':
    print(n1,'-',n2,'=',subtract(n1,n2))
elif choice == 'c':
    print(n1,'x',n2,'=',multiply(n1,n2))
elif choice == 'd':
    print(n1,'/',n2,'=',divide(n1,n2))
else:
    print("NUH UH UH YOU HAVE SELECTED SOMETHING THAT IS NOT A NUMBER OR YOU HAVE NOT SELECTED FROM A B C OR D")