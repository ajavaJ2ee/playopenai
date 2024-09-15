from collections import deque


# Efficient and are Thread safe


friends=deque(('Rolf','Jen','Charlie'))
friends.append('Jose')
print(friends)
friends.appendleft('Abhi')
print(friends)

friends.pop()
print(friends)
friends.popleft()
print(friends)



