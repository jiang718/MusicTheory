
z = int(input()[0])
for g in range(z):
    n = int(input()[0])
    print("n", n)
    a = [int(x) for x in input().split()]
    print("a", a)
    b = [0 for x in range(6)]
    c = [0 for x in range(12)]
    for i in range(0, n):
        for j in range(i + 1, n):
            x = ((a[i]-a[j]-1)%12+12)%12 + 1
            if x > 5:
                x = 12 - x
            b[x - 1] = b[x - 1] + 1
    for i in range(0, n):
        for j in range(0, n):
            y = (a[i] + a[j]) % 12
            c[y] = c[y] + 1
    print("Inverval Vector: ", b)
    print("Index Vector: ", c)