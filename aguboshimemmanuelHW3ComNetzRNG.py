print ('  ' * 20)
print(' Aguboshim, Emmanuel | 3061569 | eagubosh@uni-bremen.de ' )
print(' Communication Network - Homework III - Discrete Event Simulation and Random Number Generators')
print(' Python version 3.7')


# To implement this we first make the LCG, and then use the values as the seeds to finally implement the mixed Fibonacci:
# LCG algorithm first is: dn+1 = (adn + c) mod m
# a, dn, c, and m values were chosen to follow Hull-Dobell Theorem:
# Compute LCG with these parameters
# Obtain (29-1) distinct random numbers.
# Use this as seed to obtain the next (k-a), (k-b), and (k-1) values
# The result of this is appeneded onto a list called seed (seed here is the list of the 28 lcg numbers + other newly generated ones),
# ...and yet is still appended to a (empty) list called FibRNG. The FibRNG will contain random values with index 29 till 1029. i.e 1000 random numbers.
# Iteration is made from 29 to 1029 also.
# Here, the displayed values are just to make the print a lot easier to view. Prints on a 50 interval scale.

# e = multiplier
# c = incrementor
# m = modulo

print ('__' * 20)
print ('#Exercise 1b & 1c')

#import random
import numpy as np
import scipy.stats
import scipy
#from scipy.stats import chisquare
#import matplotlib.pyplot as plt

a = 27
viMod = pow(2,24)
ciMod = pow(2,32)
diMod = pow(2,a)
p = pow(2,18)


def lcg (e = 101427, c = 321, Xo = 123456789):
    LCG_list = []
    for i in range(0,28):
        Xo = (e*Xo + c)% p
        LCG_list.append (Xo)
    return LCG_list

seed = lcg()

print(f"{'   '*20} \n Length of seed : {len(seed)}")
print("\n Seed :", seed)

def mFibRNG (a = 27, b = 25, M = 3061569):
    FibRN = []
    #vi_list = []
    seed = lcg()
    for k in range(28,1028):
        vi = ((seed[k - a]) - (seed[k - b]))% viMod
        ci = ((seed[k - 1]) - M) % ciMod
        di = (vi - ci) % diMod
        FibRN.append (di)
        seed.append(di)
    return FibRN

fib = (mFibRNG())
N = 10
fib = (mFibRNG())

i = 0
inc = 50
print ('__' * 30)
print(f"{'  ' * 30} \n The random vlaues from the Mixed Fibonacci Generator are as below (grouped for better view):")
print ('  ' * 30)
while i<len(fib)-1:
    print(f" Elements {i} to {inc} : {fib[i:inc]} \n")
    i = inc
    inc +=50


#****************************************
# Here, the Chi-Squared Test starts:
print ('__' * 20)
print ('#Exercise 1d')

r_ange = max(fib) - min(fib)
ClassWidth = round(r_ange/N)

print("\n Range :", r_ange)
print ("\n The Maximum number is :", max(fib))
print ("\n The Minimum number is :", min(fib))
print("\n The ClassWidth is :", ClassWidth)

total  = 0
interval = []
interval2 = []
for i in range(0, 11):
    total = total + ClassWidth
    interval.append(total)
#print (interval)  #///To print the intervals expected

print ('__' * 30) #//Just to draw a line:
print ("\n The 10 Class intervals are listed as:")
x1 = [interval[0], interval[1] - 1]
x2 = [interval[1], interval[2] - 1]
x3 = [interval[2], interval[3] - 1]
x4 = [interval[3], interval[4] - 1]
x5 = [interval[4], interval[5] - 1]
x6 = [interval[5], interval[6] - 1]
x7 = [interval[6], interval[7] - 1]
x8 = [interval[7], interval[8] - 1]
x9 = [interval[8], interval[9] - 1]
x10 = [interval[9], max(fib)]

print (x1)
print (x2)
print (x3)
print (x4)
print (x5)
print (x6)
print (x7)
print (x8)
print (x9)
print (x10)

#*********************************
def make_frequency_distribution(sequence):
    return np.histogram(sequence)

distribution = make_frequency_distribution(fib)
#print(distribution)  ##****Uncomment to view.

print ('__' * 20)
Obs = distribution[0]
print ("\n The observed distribution is :", Obs)

expected = len(fib)/N
Exp = [expected, expected, expected, expected, expected, expected, expected, expected, expected, expected]
print ("\n The expected distribution is :", Exp)


# Chi_Square formular implementation:
D = scipy.stats.chisquare(Obs, Exp, 9)
print ("\n The D statistics is:", D[0])


#***plt.hist(distribution, bins="auto")
#plt.show()
print ('__' * 20)
chisq = 14.68

print ("\n From the Chi-Sqaured distribution table, we see that at DegreeOfFreedom = 9, and P_Value = 0.10, the ChiSquared Value is:", chisq)

if D[0] < chisq:
    print (' Yes, accept at 90% confidence level')
else:
    print (' No, not accept at 90% confidence level')


print ('__' * 20)
print ('#Exercise 2a')
print ('  ' * 20)
#### Exercise 2a:

a2 = 7
c2 = 11
m2 = 9
## Xo == Xo2
Xo2 = 3061569
LCG_list = [Xo2]
for i in range(1,20):
    Xo2 = (a2*Xo2 + c2)% m2
    LCG_list.append (Xo2)
    print (LCG_list)

    ### To print the first 20 random numbers, X0 incluzive
LCGrn = LCG_list[0:19]
print ("then, the first 20 random numbers, Xo incluzive is: ", LCGrn)


