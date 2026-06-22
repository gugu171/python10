try:
    number = int(input("Enter a number : "))
    print("The number you typed is",number)
except ValueError as ex:
    print(ex)

