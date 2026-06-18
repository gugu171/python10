orgnum = int(input("Enter your number : "))
power = int(input("Enter the number you want it powered by : "))
result = 1
for i in range(power):
    result = result * orgnum

print(result)
