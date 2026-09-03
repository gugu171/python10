from abc import ABC, abstractmethod

class animal(ABC):

    def move(self):
        pass

class Human(animal):
    def move(self):
        print("I KANN WAK AN ROON")

class snek(animal):
    def move(self):
        print("I SLITEER")
class dogo(animal):
    def move(self):
        print("I WAK ON FUR LIIGS ANT BORK")
class leno(animal):
    def move(self):
        print("MEKANNRAUR")

r = Human()
r.move()
k = snek()
k.move()
r = dogo()
r.move()
k = leno()
k.move()