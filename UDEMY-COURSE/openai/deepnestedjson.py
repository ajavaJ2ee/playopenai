import json

# load the JSON object from a file or string
json_obj = json.load(json_file)

# define a function to filter the JSON object
def filter_json(json_obj, key, value):
  # check if the JSON object is a dictionary
  if isinstance(json_obj, dict):
    # iterate over the keys in the dictionary
    for k, v in json_obj.items():
      # if the key matches the filter key, return the value
      if k == key and v == value:
        return v
      # otherwise, call the function recursively on the value
      else:
        return filter_json(v, key, value)
  # if the JSON object is a list, call the function recursively on each element
  elif isinstance(json_obj, list):
    return [filter_json(elem, key, value) for elem in json_obj]
  # if the JSON object is not a dictionary or list, return None
  else:
    return None

# call the filter function on the JSON object
filtered_json = filter_json(json_obj, 'key', 'value')
