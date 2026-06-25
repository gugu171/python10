import random
playing = True
number = str(random.randint(0,9))

print("BONJOUR VELCOME TO DA RANDUM NUMBAR GAME WHERE I WIL BE CHOSING A RANDUM NUMBAR FROM 0 TU 9")
print("ZE GAME ENDING VHEN YU GAT 1 HEARO")
while playing:
    guess = input("ENTAH A NUMBAR : ")
    if guess == number:
        print("YU GOT THE ANSER KORRACT! YOU GET 1 HEARO AND GAME IS OVAR!!!!11!!11!!!")
        print("ZE NUMBAR WAS",number)
        break
    
    else:
        print("OWH NEIN! YUR ANSER WAS INKORRACT. TRY AGIN!")