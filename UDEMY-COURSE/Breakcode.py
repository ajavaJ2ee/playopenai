def power_of_two():

    try:
        user_input = input('Please enter a number: ')
        n = float(user_input)
        n_square = n ** 2
        return n_square
    except ValueError:
        return f'This is not valid input'

print(power_of_two())
print(power_of_two())