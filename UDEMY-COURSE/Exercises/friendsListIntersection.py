#****** Abhi Trial***
# friends_list=[]
# i=0
# while i<3:
#     user_input = input("Enter friend name:")
#     friends_list.append(user_input)
#     i= i+1
# print(friends_list)
#
# friends_open= open('friends.txt','r')
# friends_content=friends_open.read()
#
#
# for friend in friends_list:
#     new_list = []
#     if friend in friends_content:
#     new_list.append(friends_list)
#     print(new_list)

# Modified
#the above
new_friends_list=[]
i=0
while i<3:
    user_input = input("Enter friend name:")
    new_friends_list.append(user_input)
    i= i+1
print(f"New Friends:{new_friends_list}")

new_friends_list_set= set(new_friends_list)
print(f"Set of new_friends_list_set is:{new_friends_list_set}")

friends_file= open('friends.txt','r')
friends_file_list=[line.strip() for line in friends_file.readlines()]

print(f"Friends from file:{friends_file_list}")
friends_file_list_set= set(friends_file_list)
print(f"Set of friends_file_list_set is:{friends_file_list_set}")

friends_intersection=new_friends_list_set.intersection(friends_file_list_set)
print(f"Set of friends_intersection is:{friends_intersection}")


#COde Implementation
friends = input('Enter three friend names, separated by commas:').split(',')


people= open('friends.txt','r')
people_nearby=[line.strip() for line in people.readlines()]

people.close()

friends_set = set(friends)
people_nearby_set= set(people_nearby)

friends_nearby_set= friends_set.intersection(people_nearby_set)

nearby_friends_file=open('nearby_friends.txt','w')

nearby_friends_file.write(friends_nearby_set)

nearby_friends_file.close()



