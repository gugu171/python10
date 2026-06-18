import math,os

radius = float(input("Enter the radius of your circle : "))
circumofcircle = 2 * math.pi * radius
os.system('cls' if os.name == 'nt' else 'clear')
print("The circumference of your circle is",circumofcircle)