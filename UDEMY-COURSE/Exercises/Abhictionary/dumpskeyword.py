import json
#json.dumps() function converts a Python object into a json string.

Dictionary={
    1:'Apple',
    2:'Boy'
}

json_string=json.dumps(Dictionary)

print(json_string)
