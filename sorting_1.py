l = [4, 6, 1, 9, 4, 3, 3, 5, 6]

for i in range(len(l)):
    for j in range(i + 1, len(l)):
        if l[i] > l[j]:
            l[i], l[j] = l[j], l[i]

print(l)