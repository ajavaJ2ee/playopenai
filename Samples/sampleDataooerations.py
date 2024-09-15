
names_list=["Abhi","Sai","Anir"]

names_tuple=("Abhi","Sai","Anir")

names_dictionary={'Abhi':1, 'Sai':2, 'Anir':'3'}

print(names_list.pop())
print(names_tuple.index('Abhi'))
print(names_dictionary.pop('Abhi'))
print(names_dictionary)

tuple_any=(1,)
print(any(tuple_any))