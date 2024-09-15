from collections import Counter

device_temperatures=[12.5,15.5,13.5,14.5,15.5]

temp_counter=Counter(device_temperatures)
print(temp_counter[15.5])
