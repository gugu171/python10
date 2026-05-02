import random

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
num3 = int(input("Enter num3: "))

numlist = [num1, num2, num3]

choice = input("Type 'random' to mix the numbers: ")

if choice.lower() == 'random':
    random.shuffle(numlist)
    print("Your mixed numbers are:", numlist[0], numlist[1], numlist[2])
else:
    print("Wrong word :slapping_face_emoji:. Your numbers will not be mixed. Here are the numbers as when you ordered them:", num1, num2, num3)