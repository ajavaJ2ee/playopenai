from collections import defaultdict


coworkers=[('Rolf','MIT'),('Jen','Cambridge'),('Rolf','Cambridge'),('Charlie','Manchester')]

alma_matters=defaultdict(list)

for coworker,place in coworkers:
    alma_matters[coworker].append(place)


print(alma_matters)
print(alma_matters['Rolf'])
print(alma_matters['Anne'])


#-------2------
