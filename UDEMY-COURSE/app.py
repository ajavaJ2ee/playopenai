class Car:
    def __init__(self, make, model):
        self.make=make
        self.model=model
    def __repr__(self):
        return f'<Car {self.make} {self.model}>'

class Garage:
    def __init__(self):
        self.cars =[]

    def __len__(self):
        return len(self.cars)

    def add_cars(self,newcar):
        if not isinstance(newcar,Car):
            raise TypeError(f'Tried to add a {newcar.__class__.__name__} to the garage')
        self.cars.append(newcar)



ford= Garage()
newcar = Car('Ford', 'Fiesta')
ford.add_cars(newcar)

print(len(ford))


# TypeError
# def count_from_zero_to_n(n):
#     if x<0:
#         raise ValueError(f'Value should be greater than zero')
#     for x in range(0, n+1):
#         print(x)