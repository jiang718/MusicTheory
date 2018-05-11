# 12 tones
# C3 -- E5 [0..28]
# A script for generating different music tunings

import math

def printData(a, n, s):
    print(s+':')
    for i in range(0,n):
        print(name[i % 12]+str(i / 12 + 3)+' : '+str(a[i]))

n = 29
y = pow(2, 1.0/12)
a = [0 for i in range(0, n)]
a[0] = 132.0
name = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
for i in range(1, n):
    a[i] = a[i-1]*y


x = 132.0
b = [0 for i in range(0, n)]
# Pythagorean tuning
pythagorean = [1.0, 256/243.0, 9/8.0, 32/27.0, 81/64.0, 4/3.0, 729/512.0, 3/2.0, 128/81.0, 27/16.0, 16/9.0, 243/128.0]
for i in range(0, n):
    b[i] = x * (pythagorean[i % 12] * pow(2, i/12))



# just tuning
c = [0 for i in range(0, n)]
just = [1.0, 16/15.0, 9/8.0, 6/5.0, 5/4.0, 4/3.0, 45/32.0, 3/2.0, 8/5.0, 5/3.0, 16/9.0, 15/8.0]
for i in range(0, n):
    c[i] = x * (just[i % 12] * pow(2, i / 12))

printData(a, n, '12-tempered')
print('\n')
printData(b, n, 'pythagorean')
print('\n')
printData(c, n, 'just')
