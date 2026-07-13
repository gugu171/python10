basket_1 = {'apple', 'banana', 'mango', 'apple', 'grape'}
basket_2 = {'mango', 'kiwi', 'banana', 'kiwi'}

print("Basket 1:",basket_1)
print("Basket 2:",basket_2)

basket_1.add('orange')
print("Basket 1 ayfter edits",basket_1)

commonfruits = basket_1.intersection(basket_2)
print("Fruits in both baskets",commonfruits)

import array as arr
fruitcounts = arr.array('i', [3,5,2,4])
print("Fruit counts array",fruitcounts)

fruitcounts.insert(0,1)
fruitcounts.append(6)
print("Fruit counts after edits:",fruitcounts)

countof4 = fruitcounts.count(4)
print("Number of times 4 appears:",countof4)

fruitcounts.reverse()
print("Reversed fruit counts array:",fruitcounts)

print("")
print("===== CLASS FRUIT BASKET ORGANIZER =====")
print("Basket 1:",basket_1)
print("Basket 2:",basket_2)
print("Common fruits:",commonfruits)
print("Fruit count:",fruitcounts)
print("=========================================")