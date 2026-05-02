print("Welcome to gugu171's Luxury Vehicle Dealership (for cars, only sport sedans)!")
print("1: Car")
print("2: Motorbike")
print("3: Aeroplane")
select=int(input("Select your vehicle: "))
if select == 1:
    print("What type of car?")
    print("1. Ferrari")
    print("2. Porsche")
    sel1=int(input("Enter your choice : "))
    if sel1 == 1:
        print("You have selected Ferrari. Now which type of Ferrari?")
        print("1. Ferrari 12 Cilindri")
        print("2. Ferrari 849 Testarossa")
        sel2=int(input("Enter your choice : "))
        if sel2 == 1:
            print("You have selected the Ferrari 12 Cilindri. Great choice! What colour do you want?")
            print("1: Red")
            print("2: Yellow")
            sel3=int(input("Enter your choice: "))
            if sel3 == 1:
                print("You have selected red. Thank you! That will be £520,000")
            else:
                print("You have selected yellow. Thank you! That will be £505,000")
        else:
            print("You have selected the Ferrari 849 Testarossa. Great choice! What colour do you want?")
            print("1: Red")
            print("2: Yellow")
            sel4=int(input("Enter your choice: "))
            if sel4 == 1:
                print("You have selected red. Thank you! That will be £459,999.")
            else:
                print("You have selected yellow. Thank you! That will be £449,999.")
    else:
        print("You have selected Porsche. Now which type of Porsche?")
        print("1. Porsche 718 GT4RS Weissach Package")
        print("2. Porsche 918 Spyder Weissach Package")
        sel5=int(input("Enter your choice : "))
        if sel5 == 1:
            print("You have selected the Porsche 718 GT4RS Weissach Package. Great choice! What colour do you want?")
            print("1: Arctic Grey")
            print("2: Shark Blue")
            sel6=int(input("Enter your choice: "))
            if sel6 == 1:
                print("You have selected Arctic Grey. Thank you! That will be £150,000")
            else:
                print("You have selected Sharj Blue. Thank you! That will be £134,999")
        else:
            print("You have selected the Porsche 918 Spyder Weissach Package. Great choice! What colour do you want?")
            print("1: Liquid Silver")
            print("2: Chrome Blue")
            sel7=int(input("Enter your choice: "))
            if sel7 == 1:
                print("You have selected Liquid Silver. Thank you! That will be £6,049,000.")
            else:
                print("You have selected Chrome Blue. Thank you! That will be £6,075,000.")
elif select == 2:
    print("You have selected Motorbike. Which brand?")
    print("1. Triumph Trident")
    print("2. BMW")
    sel8=int(input("Enter your choice: "))
    if sel8 == 1:
        print("You have selected Triumph Trident. Which model?")
        print("1. Trident 660")
        print("2. Trident Tiger Sport 600")
        sel9=int(input("Enter your choice: "))
        if sel9 == 1:
            print("You have selected the Trident 660. Which colour?")
            print("1. Snowdonia White")
            print("2. Cosmic Yellow")
            sel10=int(input("Enter your choice: "))
            if sel10 == 1:
                print("You have chosen Snowdonia White. That will be £8,095")
            else:
                print("You have chosen Cosmic Yellow. That will be £8,300")
    else:
        print("You have selected BMW. Which model?")
        print("1. BMW M1000 XR")
        print("2. BMW S1000 RR")
        sel11=int(input("Enter your choice: "))
        if sel11 == 1:
            print("You have selected the BMW M1000 XR. Which colour?")
            print("1. Aurelius Green")
            print("2. Black Storm")
            sel12=int(input("Enter your choice: "))
            if sel12 == 1:
                print("You have chosen Aurelius Green. That will be £28,120.")
            else:
                print("You have chosen Black Storm. That will be £28,120.")
        else:
            print("You have selected the BMW S1000 RR. Which colour?")
            print("1. M Package")
            print("2. Black Storm")
            sel13=int(input("Enter your choice: "))
            if sel13 == 1:
                print("You have chosen the M Package. That will be £23,060.")
            else:
                print("You have chosen Black Storm. That will be £18,050.")
else:
    print("You have selected Aeroplane. Now which one?")
    print("1. Airbus A350")
    print("2. Boeing 787")
    sel14=int(input("Enter your choice: "))
    if sel14 == 1:
        print("You have chosen the Airbus A350. Now which variant?")
        print("1. A350-900")
        print("2. A350-1000")
        sel15=int(input("Enter your choice: "))
        if sel15 == 1:
            print("You have chosen the Airbus A350-900. Now which livery?")
            sel16=input("Enter your airline's livery: ")
            print("You have chosen",sel16,"'s livery. This will be £200,000,000 ")
        else:
            print("You have selected the Airbus A350-1000. Now which livery?")
            sel17=input("Enter your airline's livery: ")
            print("You have chosen",sel17,"'s livery. This will be £355,000,000 ")
    else:
        print("You have selected the Boeing 787. Now which variant?")
        print("1. 787-8")
        print("2. 787-9")
        print("3. 787-10")
        sel18=int(input("Enter your choice"))
        if sel18 == 1:
            print("You have selected the Boeing 787-8. Now which livery?")
            sel19=input("Enter your airline's livery: ")
            print("You have chosen",sel19,"'s livery. This will be £248,000,000 ")
        elif sel18 == 2:
            print("You have selected the Boeing 787-9. Now which livery?")
            sel20=input("Enter your airline's livery: ")
            print("You have chosen",sel20,"'s livery. This will be £295,000,000 ")
        else:
            print("You have selected the Boeing 787-10. Now which livery?")
            sel21=input("Enter your airline's livery: ")
            print("You have chosen",sel21,"'s livery. This will be £340,000,000 ")
print("Thank you for shopping at gugu171's Luxury Vehicle Dealership! Hope to see you back soon!")