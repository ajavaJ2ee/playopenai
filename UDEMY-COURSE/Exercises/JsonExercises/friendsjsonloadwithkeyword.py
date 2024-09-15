import json



with open('friends.txt','r') as f:
    f_contents= json.load(f)
    print(f'{f_contents}')