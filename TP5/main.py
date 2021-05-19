def h1(k):
    return k

def h2(k):
    return 1 + (k % (m-1))

def h(k, i):
    return ((h1(k) + i * h2(k)) % m)

m = 11

k = 59
i = 2

print(h(k, i))