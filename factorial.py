def factorial(x):
    """This is a recursive function to find the factorial of an integer"""

    if x==0:
        return 0
    elif x==1:
        return 1
    else:
        return x*factorial(x-1)
    
print(factorial.__doc__)
print("The factorial for 0:",factorial(0))
print("The factorial for 1:",factorial(1))
print("The factorial for 2:",factorial(2))
print("The factorial for 5:",factorial(5))
print("The factorial for 10 is:",factorial(10))