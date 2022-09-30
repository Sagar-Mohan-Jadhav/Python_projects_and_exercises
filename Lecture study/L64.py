class Garage:
    def __init__(self):
        self.cars = []

    def __getitem__(self, item):
        return self.cars[item]


gar = Garage()
gar.cars.append('ford')
gar.cars.append('mg')
print(gar[0])
