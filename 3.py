with open('file1.txt', 'w+') as fo:
    for j in range(1, 31):
        for i in range(1, 31):
            k = (j + i) * (j + i + 1) // 2 + j
            fo.write(str(k) + ' ')
        fo.write('\n')