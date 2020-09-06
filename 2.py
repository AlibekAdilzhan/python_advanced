m, n, s = 3, 3, 0

r = [[i * j for j in range(m)] for i in range(n)]

for i in range(n):
    s += sum(r[i])

print(r)