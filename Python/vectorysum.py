import sys
from datetime import datetime
import numpy

def numpysum(n):
    a = numpy.arange(n) ** 2
    b = numpy.arange(2) ** 3
    c = a+b
    return c

def pythonsum(n):
    a = range(n)
    b = range(n)
    c = []

    for i in range(len(a)):
        a[i] = i ** 2
        b[i] = i ** 3
        c.append(a[i] + b[i])
    return c

size = int(sys.argv[1])

start = datetime.now()
c = pythonsum(size)
delta = datetime.now() - start
print "The last 2 elements of sum", c[-2:]
print "PythonSum elapsed time in microseconds", delta.microseconds

start = datetime.now()
c = pythonsum(size)
delta = datetime.now() - start
print "The last 2 elements of sum", c[-2:]
print "NumpySum elapsed time in microseconds", delta.microseconds

