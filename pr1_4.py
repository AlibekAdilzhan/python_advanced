x1, y1 = map(float, input())
x2, y2 = map(float, input())
x3, y3 = map(float, input())

ans = (y2 - y1) / (x2 - x1) * x3 - (y2 - y1) * x1 / (x2 - x1) + y1

if ans > y3:
    print('above')

else:
    print('under')