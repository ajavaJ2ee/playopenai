import json

cars_list=[
    {
        "make":"bmw",
        "model":"528i"
    }
]

cars= open("cars.txt","w")

json.dump(cars_list,cars)

cars.close()