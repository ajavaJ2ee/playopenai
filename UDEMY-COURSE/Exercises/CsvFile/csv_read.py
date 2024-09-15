

read_csv= open('csv_data.txt','r')

lines= read_csv.readlines()

read_csv.close()

lines = [line.strip() for line in lines[1:]]

for line in lines:
    person_data=line.split(',')
    name=person_data[0].title()
    age=person_data[1]
    address=person_data[2].capitalize()
    print(person_data)

