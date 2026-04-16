h=float(input("Enter your height: "))
w=float(input("Enter your weight: "))
bfr=w/(h/100)**2
bmi=round(bfr,2)
print("Your BMI is",bmi)
if bmi<18.4:
    print("You are underweight")
elif bmi<24.9:
    print("You are healthy")
elif bmi<29.9:
    print("You are overweight")
elif bmi<34.9:
    print("You are severely overweight")
elif bmi<39.9:
    print("You are obese")
else:
    print("You are severely obese")