

def listofnumbers():
    i=0
    while i<=100:
        yield i
        i+=1

g=listofnumbers()
print(next(g))
print(next(g))
# Prints from 2
print(list(g))

print([x*2 for x in listofnumbers()])

