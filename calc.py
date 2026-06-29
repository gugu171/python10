try:
    n1 = float(input("Enter number 1 (guess what...it can be a decimal too!) : "))
    n2 = float(input("Enter number 2 (guess what...this can also be a decimal!) : "))
    op = input("Good. Now choose an operation (from *, /, + and -) : ")
except ZeroDivisionError:
    print("You can't divide by 0.")
except ValueError:
    print("Oops! yu got a value error :P. You must have typed a letter or something lol")
def add(n1,n2):
    return(n1 + n2)
def subtract(n1,n2):
    return(n1 - n2)
def multiply(n1,n2):
    return(n1 * n2)
def divide(n1,n2):
    return(n1 / n2)

if op == '/':
    print(n1,"/",n2,"=",divide(n1,n2))
elif op == '*':
    print(n1,"*",n2,"=",multiply(n1,n2))
elif op == '+':
    print(n1,"+",n2,"=",add(n1,n2))
else:
    print(n1,"-",n2,"=",subtract(n1,n2))



    




