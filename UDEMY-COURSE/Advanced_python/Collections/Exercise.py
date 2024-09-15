from collections import defaultdict
from collections import OrderedDict
from collections import namedtuple
from collections import deque

def task1():
   dd=defaultdict(lambda:'Unknown')
   dd['Alan']='Manchester'
   return dd



#print(task1())

o=OrderedDict([
        ('Alan', 'Manchester'),
        ('Bob', 'London'),
        ('Chris', 'Lisbon'),
        ('Dan', 'Paris'),
        ('Eden', 'Liverpool'),
        ('Frank', 'Newcastle')
    ])
def task2(arg_od):
    o.popitem()
    o.popitem(False)
    o.move_to_end('Bob')
    o.move_to_end('Dan',last=False)
    return o


#print(task2(o))


def task3(name,club):
    player_named = namedtuple('Player', ['name', 'club'])
    player=player_named(name,club)
    return player

#print(task3('Abhi','WC'))


deque_name=deque(('Alan','Bob','Charlie'))
def task4(arg_deque):
    arg_deque.pop()
    arg_deque.append(arg_deque.popleft())
    arg_deque.appendleft('Zack')
    return arg_deque


print(task4(deque_name))