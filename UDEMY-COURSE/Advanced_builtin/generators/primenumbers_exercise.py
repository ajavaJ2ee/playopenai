


def primenumbers(num):
    for i in range(2, num):
        for j in range(2,i):
            if (i%j)==0:
                break
        else:
            yield i

g=primenumbers(20)

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

