import json


cars= [
    {'make':'Ford','model':'Fiesta'},
    {'make':'Fiat','model':'Punto'}
]
file= open('cars.json','w')

json.dump(cars,file)

file.close()
