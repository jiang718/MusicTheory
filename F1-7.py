from random import randint
a = ["F", "Gm", "Am", "Bb", "C", "Dm", "Edim"]
k = [0 for i in range(7)]
prev = 0
print("key = F")
while True:
    p = randint(1,7)
    while k[p - 1] == 1 or p == prev:
        p = randint(1,7)
    print(p, end='')
    k[p - 1] = 1
    prev = p
    s = 0
    for i in range(7):
        if k[i] == 1:
            s = s + 1
    if s == 7:
        k = [0 for i in range(7)]
    now = input()
    print(a[p - 1])
    print()
    if now != "": 
        break
