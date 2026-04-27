myltr=input("Enter something: ")
if myltr.isalpha():
    print(myltr,"is part of the alphabet")
else:
    print(myltr,"is not part of the alphabet")

chr=input("Enter a character: ")
alphabet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
if chr not in alphabet:
    print(chr,"is not in the alphabet")
else:
    print(chr,"is in the alphabet")
