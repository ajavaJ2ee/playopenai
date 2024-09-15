friends=['Robin','Adam','Eva','Rolf']

friends_map= map(lambda x: x.lower(),friends)

friends_list =[friend.lower() for friend in friends]

friends_generator_comprehension=(friend.lower() for friend in friends)

print(list(friends_map))

print(friends_list)
print(list(friends_generator_comprehension))


#2

class User:
    def __init__(self,username,password):
        self.username=username
        self.password=password
    @classmethod
    def from_dict(cls,data):
        return cls(data['username'],data['password'])

users=[
    {'username':'Abhinai1','password':'123'},
    {'username':'Abhinai2','password':'1234'}
]

users_data = [User.from_dict(user) for user in users]
users_map=map(User.from_dict,users)
print(users_map)