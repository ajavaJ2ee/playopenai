#Not very useful as dict are maintaining the order
from collections import OrderedDict


o=OrderedDict()
o['Rolf']=6
o['Rolf2']=2
o['Rolf3']=5

print(o)

o.move_to_end('Rolf')

print(o)

o.move_to_end('Rolf3',last=False)

print(o)

o.popitem()

print(o)


