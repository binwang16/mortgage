si = 0
for i in range(1, 1300):
    ai = 116.74-0.19*i
    si = si + ai
    if (i%52 == 0):
        print("{0} : {1} : {2}".format(i, ai, si))



