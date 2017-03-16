# Graham scan (Andrew's variant)
# Jacob Morra, March 14 2017

import numpy as np
import matplotlib.pyplot as plt

"""
function takes 3 points (p1,p2,p3), returns direction as CW (>0), CCW (<0), colinear
"""
def isCW(p1, p2, p3):
    return (p2[1] - p1[1]) * (p3[0] - p1[0]) - (p2[0] - p1[0]) * (p3[1] - p1[1])


def upper(X):
    '''first, sort the list of coordinates from left-right, then down-up'''
    X.sort()
    i=0
    H1 = []
    print "X = ", X

    while i < len(X):
        '''while H1 has 2+ elements'''
        while len(H1) >= 2:
            '''if direction of last 3 points is CCW, pop last point'''
            if not isCW(H1[-2], H1[-1], X[i]) >= 0:
                H1.pop()
                print "H1 pop"
            else:
                break
        H1.append(X[i])
        print "H1 = ", H1
        i += 1
    return H1


def lower(X):
    '''first, sort the list of coordinates from left-right, then down-up'''
    X.sort()
    j=0
    H2 = []
    print "X = ", X

    while j < len(X):
        '''while H2 has 2+ elements'''
        while len(H2) >= 2:
            '''if direction of last 3 points is CW, pop last point'''
            if isCW(H2[-2], H2[-1], X[j]) >= 0:
                H2.pop()
                print "H2 pop"
            else:
                break
        H2.append(X[j])
        print "H2 = ", H2
        j += 1
    return H2


# plot
N = 6
x = np.random.randint(-5, 5, N)
y = np.random.randint(-5, 5, N)

plt.scatter(x, y)

H1 = upper([(x[0], y[0]), (x[1], y[1]), (x[2], y[2]), (x[3], y[3]), (x[4], y[4]), (x[5], y[5])])
H2 = lower([(x[0], y[0]), (x[1], y[1]), (x[2], y[2]), (x[3], y[3]), (x[4], y[4]), (x[5], y[5])])

print H1
print H2

plt.plot(*zip(*H1))
plt.plot(*zip(*H2))
plt.show()