import sys
def modn(x, n):
    return (x % n + n) % n

def inverse(p):
    q = []
    for i in range(len(p)):
        q.append(modn(12 - p[i], 12))
    return q

def tozero(q):
    p = q
    d = p[0]
    for i in range(len(p)):
        p[i] = modn(p[i] - d, 12)
    return p

def normal(q):
    p = sorted(q)
    n = len(q)
    now = 1000000000000
    choose = 0
    for i in range(n):
        start = i
        end = modn(start + n - 1, n)
        val = 0
        for j in range(n - 1):
            dis = modn(p[end] - p[start], 12)
            val = val + dis * 12
            end = modn(end - 1, n)
        if val < now:
            now = val
            choose = start
    z = []
    for i in range(n):
        t = modn(i + choose, n)
        z.append(p[t])
    return z

def bigger(x, y):
    n = len(x)
    for i in range(0, n - 1):
       if x[n - i - 1] > y[n - i - 1]:
           return True
    return False 
    
    
def sc(p):
    x = normal(p)
    y = tozero(x)
    z = tozero(normal(inverse(x)))
    if bigger(y, z):
        return z
    return y
    


p = [int(x) for x in input().split()]
print(sc(p))
