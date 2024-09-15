class UncountableError(ValueError):
    def __init__(self,wrong_value):
        super().__init__(f'Invalid value for n,{wrong_value}.n must be greater than 0')



# do not change anything in the count_from_zero_to_n() function
# you may expect your UncountableError work in the following way
def count_from_zero_to_n(n):
    if n < 1:
        raise UncountableError(n)
    for x in range(0, n + 1):
        print(x)


count_from_zero_to_n(-10)