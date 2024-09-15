import json

my_json_string='[{"name":"Abhinai","age":"32"}]'

names= json.loads(my_json_string)

print(names[0]['name'])