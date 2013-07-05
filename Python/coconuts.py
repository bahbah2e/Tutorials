#Write a program that will find the initial number
#of coconuts. 

def f(n):
    return (n-1) / 5.0 * 4

def f6(n):
    for i in range(6):
        n = f(n)
    return n 

def is_int(n):
    return abs(n-int(n)) < 0.0000001

def update(mean1, var1, mean2, var2):
    new_mean = ((mean1 * var2) + (mean2 * var1)) / (var1 + var2)
    new_var = 1 / ((1/var1) + (1/var2))
    return [new_mean, new_var]

def predict(mean1, var1, mean2, var2):
    new_mean = mean1 + mean2
    new_var = var1 + var2
    return [new_mean, new_var]

measurements = [5., 6., 7., 9., 10.]
motion = [1., 1., 2., 1., 1.]
measurement_sig = 4.
motion_sig = 2.
mu = 0
sig = 0.0000000001

#Please print out ONLY the final values of the mean
#and the variance in a list [mu, sig]. 

for i in range(len(measurements)):
    measurement = measurements[i]
    motion_last = motion[i]
    [mu, sig] = update(mu, sig, measurement, measurement_sig)
    print "update: %s" % [mu,sig]
    [mu, sig] = predict(mu, sig, motion_last, motion_sig)
    print "predict: %s" % [mu,sig]