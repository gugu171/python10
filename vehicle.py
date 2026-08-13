class vehicletype:
    def __init__(self, brand, max_speed):
        self.brand = brand
        self.max_speed = max_speed

    def showdetails(self):
        print("Brand:", self.brand)
        print("Max Speed:", self.max_speed, "km/h")
class car(vehicletype):
    def __init__(self, model, seats, brand, max_speed):
        self.model = model
        self.seats = seats
        super().__init__(brand, max_speed)
    def showdetails(self):
        print("Model:", self.model)
        print("Seats:", self.seats)
        super().showdetails()
    def fueltype(self, fuel):
        print(self.model, "uses", fuel)

my_car = car("Gorble Tang", 49000, "Mitsubanchai", 'More dan youlll ever imgin >:D')

my_car.showdetails()
my_car.fueltype("Mercury")

print("Is dis karr a sublcass of vhicleetipe?", issubclass(car, vehicletype))
