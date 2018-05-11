def modn(x, y):
    return (x % y + y) % y

def simple_transpose(a, n):
    b = []
    for x in a:
        b.append(modn(x + n, 12))
    return b

def simple_inverse(a, n):
    b = []
    for x in a:
        b.append(modn(n - x, 12))
    return b

def series(b, c):
    s = 0
    f = [0 for i in range(12)]
    for x in b:
        f[x] = 1
    for x in c:
        f[x] = 1
    for x in f:
        if x == 1:
            s = s + 1
    if s == 12:
        return True
    return False

def compliments(a):
    ans = []
    for i in range(0, 12):
        b = simple_inverse(a, i)
        if series(a, b):
            ans.append(b) 
    return ans

def equal(a, b):
    aa = sorted(a) 
    bb = sorted(b) 
    return aa == bb

def find_trans(a):
    b = compliments(a) 
    ans = []
    for i in range(0, 12):
        for x in b:
            c = simple_transpose(a, i)
            if equal(x,c):
                ans.append([i, x])
            break
    return ans

def find_inverse(a):
    b = compliments(a)
    ans = []
    for i in range(0, 12):
        for x in b:
            c = simple_inverse(a, i)
            if equal(x,c):
                ans.append([i, x])
            break
    return ans

def find_ratro(a):
    ans = []
    for i in range(0,12):
        b = simple_transpose(a, i)
        if equal(a, b): 
            ans.append([i, b])
    return ans

def find_ratroinverse(a):
    ans = []
    for i in range(0, 12):
        b = simple_inverse(a, i)
        if equal(a, b):
            ans.append([i, b])
    return ans

        

a = [int(x) for x in input().split()]
print("compliments:")
print(compliments(a))
print("trans:")
print(find_trans(a))
print("inverse:")
print(find_inverse(a))
print("ratro:")
print(find_ratro(a))
print("ratroinverse:")
print(find_ratroinverse(a))

