import json

json_list=[]

csv_file=open('csv_file.txt','r')

for line in csv_file.readlines():
    club,city,country= line.strip().split(',')
    data={
        'club':club,
        'city':city,
        'country':country
    }
    json_list.append(data)

json_file=open('file_json.txt','w')

json.dump(json_list,json_file)

json_file.close()

