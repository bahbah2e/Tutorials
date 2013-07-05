import sys
import random
lst = range(2)

heads = 0
tails = 0
tosses = 100

tosses = int(sys.argv[-1])

while heads+tails < tosses:
    toss = random.choice(lst)
    if toss == 0:
        heads += 1
    else:
        tails += 1

print "heads", heads
print "tails", tails