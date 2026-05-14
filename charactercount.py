s=input("Enter your string : ")
a=input("Enter the character of the letter you want to check: ")
c=0
count=0
while c<len(s):
    if s[c] == a:
        count=count+1
    c=c+1
print("The number of letters in that string is:",count)