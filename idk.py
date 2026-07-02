numbers = [10, 20, 30, 40, 50]
print("Org list :",numbers)

print("First element :",numbers[0])
print("Last element :",numbers[-1])

print("Slice [1:4] :",numbers[1:4])

numbers.append(60)
numbers.insert(2, 25)
print("After appending and inserting:",numbers)

numbers.remove(40)
popped = numbers.pop()
print("After removing and popping:",numbers,"| Popped:",popped)

numbers[0] = 5
print("After update:",numbers)

print("Index of 30:",numbers.index(30))
print("Is 100 in the list? :",100 in numbers)

numbers.sort()
print("The sorted list:",numbers)
numbers.reverse()
print("The reversed list:",numbers)

print("Length:",len(numbers))
print("Sum:",sum(numbers))
print("Max",max(numbers))
print("Min",min(numbers))
