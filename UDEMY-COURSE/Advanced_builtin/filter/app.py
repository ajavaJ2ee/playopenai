def starts_with_r(friend):
    return friend.startswith('R')

friends=['Robin','Adam','Eva','Rolf']

friends_with_r=filter(starts_with_r,friends)

print(list(friends_with_r))
#print(next(friends_with_r))
#
# for friend in friends_with_r:
#     print(f'Friend:{friend}')

#2. Lambda
friends=['Robin','Adam','Eva','Rolf']

friends_with_r=filter(lambda friend: friend.startswith('R'),friends)
#Generator
friends_with_r_generator= (friend for friend in friends if friend.startswith('R'))
print(f'Generator comprehension :{list(friends_with_r_generator)}')
print(f'Lambda :{list(friends_with_r)}')


#3.
friends=['Robin','Adam','Eva','Rolf']



def custom_filter(func, iterable):
    for i in iterable:
        if func(i):
            yield i

friends_with_r= custom_filter(lambda friend: friend.startswith('R'),friends)

print(f'custom filter:{next(friends_with_r)}')




