"""
double principle weekly
total mortgage: b1 
arm: b2
frequency: b3
interest: b4
temp1 = b1*b4/(100*b3)+2*b1*b4/100*b3*b3*b2
temp2 = 2*b1*b4/100*b2*b3*b3
a(n) = temp1 - temp2 * n

"""

si = 0
for i in range(1, 1300):
    ai = 116.74-0.19*i
    si = si + ai
    if (i%52 == 0):
        print("{0} : {1} : {2}".format(i, ai, si))



