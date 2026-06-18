import os
def shutdown():
    user_choice = input("Do you want to shutdown? Type 'yes' to confirm or 'no' to return to the main interface : ")


    if user_choice == 'yes':
        os.system('cls' if os.name == 'nt' else 'clear')
        twofa = input("Alright. Ensure that all of your files are saved before shutting down. Type 'saved' to continue : ")
        if twofa == 'saved':
            print("Alright. Your computer is shutting down... ")
            power_button_input = input("Your computer has now turned off. It is now safe to press the power button ('a') on your PC. ")
            if power_button_input == 'a':
                os.system('cls' if os.name == 'nt' else 'clear')
        else:
            print("That command is not supported. Perhaps a typo?")
    elif user_choice == 'no':
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Alright. Returning to the main interface...")
    else:
        print("That command is not supported. Perhaps a typo?")
shutdown()



