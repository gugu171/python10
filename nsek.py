snack_box1 = {'chips', 'joos', 'cokies', 'chippty', 'apel'}
snack_box2 = {'cokies', 'sandmich', 'joos', 'sammcih'}
print('snakbox1 : ', snack_box1)
print('snakbox2 : ', snack_box2)

snack_box1.add('banananannananan')
print('snakbox1 aapter ading bananananannnananan', snack_box1)

comonsnak = snack_box1.intersection(snack_box2)
print("snak in bof boxies: ",comonsnak)

import array as arr
snek_conuts = arr.array('i', [4, 6, 3, 5])
print('snak conut aray: ',snek_conuts)

snek_conuts.insert(0,2)
snek_conuts.append(7)
print('snekconuts after ad item : ', snek_conuts)

conutoffiv = snek_conuts.count(5)
print('numbi of itm 5 apir: ', conutoffiv)

snek_conuts.reverse()
print('revvee snak counut aray:', snek_conuts)

print("")
print("SCHOL SNEK COUNTIR")
print('SNEK VOX 1: ',snack_box1)
print('SNEK BOX 2: ', snack_box2)
print('SHARE SNEKS: ',comonsnak)
print('SNEK CONUTS: ',snek_conuts)

