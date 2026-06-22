try:
    num1, num2 = eval(input("Enter two numbers, separated by a comma : "))
    answer = num1 / num2
    print("Result is",answer)

except ZeroDivisionError:
    print("You CANNOT put a 0 anywhere. >:(")
except SyntaxError:
    print("Yu hav rote it rong. Rite it liek dis : e.g. 1,2")
except:
    print("Rong input")
else:
    print("There are no exceptions. :D")
finally:
    print("Dis WIL xecute no mater wat. :)")
