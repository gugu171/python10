L = [4, 5, 1, 2, 9, 7, 10, 8]
print("Org list:",L)

count = 0

for i in L:
    count += 1

avg = count/len(L)

print("Sum =",count)
print("AVG =",avg)

L.sort()

print("Smallest element :",L[0])
print("Largest element:",L[-1])