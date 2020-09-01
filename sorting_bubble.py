l = [4, 6, 1, 9, 4, 3, 3, 5, 6]

for i in range(len(l) - 1):
    for j in range(len(l) - 1 - i):
        if l[j] > l[j + 1]:
            l[j], l[j + 1] = l[j + 1], l[j]

print(l)