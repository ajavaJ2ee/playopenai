# Import the json module
import json

# Define a JSON object
json_obj = {
    "name": "John",
    "age": 30,
    "address": {
        "street": "123 Main Street",
        "city": "Seattle",
        "state": "WA"
    }
}

# Define a function to filter the JSON object
def filter_json(obj, key, value):
    # Initialize an empty list to store the results
    results = []

    # Check if the object is a dictionary
    if isinstance(obj, dict):
        # Loop through the items in the dictionary
        for k, v in obj.items():
            # If the key and value match the specified key and value, add the object to the results list
            if k == key and v == value:
                results.append(obj)

            # If the value is a dictionary, recursively call the filter_json function to filter it
            if isinstance(v, dict):
                results.extend(filter_json(v, key, value))
    return results

# Filter the JSON object and print the results
results = filter_json(json_obj, "city", "Seattle")
print(json.dumps(results, indent=4))
