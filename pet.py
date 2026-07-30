class Pet:
    print('Jus a simpel pet profil')

petob = Pet()
class PetProfile:

    category = 'pet'

    def __init__(self, name, animal_type, age, favourite_food):
        self.name = name
        self.animal_type = animal_type
        self.age = age
        self.favourite_food = favourite_food

pet1 = PetProfile('Johhny', 'Guraffe', 7278, 'Cabbage')
pet2 = PetProfile('Nog', 'Zibrea', 91111092, 'Burma')

print("Johhny is a {}".format(pet1.category))
print("Nog is a {}".format(pet2.category))
print('{} is a {} and is {} years old'.format(pet1.name, pet1.animal_type, pet1.age))
print('{} likes eating {}'.format(pet1.name, pet1.favourite_food))
print('{} is a {} and is {} years old'.format(pet2.name, pet2.animal_type, pet2.age))
print('{} likes eating {}'.format(pet2.name, pet2.favourite_food))