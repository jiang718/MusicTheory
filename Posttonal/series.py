def print_format(x):
    for i in x:
        print('{:2}'.format(i), end = " ")
    print()

def print_format2(x):
    for i in x:
        print(i, end = " ")
    print()

def modn(x, n):
    return (x % n + n) % n

def notpass(x):
    f = [0 for i in range(12)]
    if len(x) < 12:
        return True
    for i in x:
        k = modn(i, 12)
        f[k] = f[k] + 1
        if f[k] > 1:
            return True
    return False
        


p = [int(x) for x in input().split()]
n = len(p)
d = p[0]

if notpass(p):
    print("not series")
else:
    for i in range(n):
        p[i] = modn(p[i] - d, n)  
    print_format(p)
    for i in range(1, n):
        row = []
        first = modn(n - p[i], n)
        dis = modn(first - p[0], n)
        for j in range(n):
            row.append(modn(p[j] + dis, n))
        print_format(row)
    print("Ordered Pitch Class Interval:")
    o = []
    for i in range(1, n):
        o.append(modn(p[i] - p[i - 1], n))
    print_format2(o)
        