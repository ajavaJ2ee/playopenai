import json
import objectpath
import pandas as pd

# df = pd.read_json("users.json")
#
# batters=df['batters']
#
# to_json=batters.to_json(orient="records")
# parsed = json.loads(to_json)
#
# print(parsed)

json_data = """
{
"problems": [{
    "Diabetes":[{
        "medications":[{
            "medicationsClasses":[{
                "className":[{
                    "associatedDrug":[{
                        "name":"asprin",
                        "dose":"",
                        "strength":"500 mg"
                    }],
                    "associatedDrug#2":[{
                        "name":"somethingElse",
                        "dose":"",
                        "strength":"500 mg"
                    }]
                }],
                "className2":[{
                    "associatedDrug":[{
                        "name":"asprin",
                        "dose":"",
                        "strength":"500 mg"
                    }],
                    "associatedDrug#2":[{
                        "name":"somethingElse",
                        "dose":"",
                        "strength":"500 mg"
                    }]
                }]
            }]
        }],
        "labs":[{
            "missing_field": "missing_value"
        }]
    }],
    "Asthma":[{}]
}]}"""

json_pd=pd.read_json(json_data)
pd_json=json_pd.to_json()

to_dict=json.loads(pd_json)
print(pd_json)
print(type(pd_json))
print(type(to_dict))
print(to_dict)


# with open("users.json","r") as file:
#     print(type(file))
#     data= json.load(file.read())
# print(type(data))
#
#
# print(f'data is:{data}')
#
# data_json=json.dumps(data,indent=3)
#
# print(type(data_json))






