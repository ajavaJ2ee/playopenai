import json



with open('friends.txt','r') as f:
    f_contents= json.load(f)
    print(f'{f_contents}')

file = open('friends.txt', 'r')

file_contents = json.load(file)

file.close()

print(file_contents['profile'][0])


cars =[
    {'make': 'Ford','model':'Fiesta1'},
    {'make':'Ford','model':'Focus1'}
]

file=open('cars.json','w')

json.dump(cars,file)

file.close()
