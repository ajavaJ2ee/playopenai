
class FirstHundredGenerator:
    def __init__(self):
        self.number = 0

    def __next__(self):
        if self.number < 100:
            current=self.number
            self.number+=1
            return current
        else:
            raise StopIteration()

class FirstHundredIterable:
    def __iter__(self):
        return FirstHundredGenerator()

print(sum(FirstHundredIterable()))

for i in FirstHundredIterable():
    print(i)

class AnotherIterable:
    def __init__(self):
        self.cars=['Ford','Fiesta']
    def __len__(self):
        return len(self.cars)
    def __getitem__(self, i):
        return self.cars[i]

for car in AnotherIterable():
    print(car)

#Generator comprehension

numbers=[x for x in [1,2,3,4]]
numbers_gen=(x for x in [1,2,3,4])
print(next(numbers_gen))
