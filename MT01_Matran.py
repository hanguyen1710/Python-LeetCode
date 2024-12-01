import numpy
m,n=[int(x) for x in input().split()]
a=[int(x) for x in input().split()]
b=numpy.reshape(a,(m,n))
for row in b:
    print(*row)

    