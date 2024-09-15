class FirstHundredGenerator:
    def __init__(self):
        self.number=0

    def __next__(self):
        if self.number<100:
            current = self.number
            self.number+=1
            return current
        else:
            raise StopIteration()

my_gen=FirstHundredGenerator()
# print(my_gen.number)
# my_gen.__next__()
# print(my_gen.number)
print(next(my_gen))
print(next(my_gen))
