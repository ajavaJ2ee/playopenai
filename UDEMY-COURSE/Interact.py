def interact():
    while True:
        try:
            user_input= int(input('Please enter a number:'))
        except ValueError:
            print('Invalid user input')
        else:
            print('{} is {}.'.format(user_input, 'even' if user_input % 2 == 0 else 'odd'))
        finally:
            user_choice=input('Do you wish to continue the Game, Y/N:')
            if user_choice != 'Y':
                print('GoodBye')
                break


print(interact())


