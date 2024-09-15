import json

Dictionary = {
    1: 'Apple',
    2: 'Boy',
    1: 'Apple',
    2: 'Boy'
}


def save_file(Dictionary, fileName):
    with open("importingownfiles.txt", "w") as fileName:
        json.dump(Dictionary, fileName)
        print("Saved contents")

fileName = open("importingownfiles.txt", "w")

save_file(Dictionary, fileName)

def read_file(fileName):
    with open("importingownfiles.txt", "r") as fileName:
        file_contents=json.load(fileName)
        print(file_contents)
        print("Printed successfully")

fileName = open("importingownfiles.txt", "r")

read_file(fileName)