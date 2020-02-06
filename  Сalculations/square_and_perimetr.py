def findSide(x1, y1, x2, y2):
    return (((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5)


x1, y1, x2, y2, x3, y3 = map(float, input().split())
a = findSide(x1, y1, x2, y2)
b = findSide(x2, y2, x3, y3)
c = findSide(x3, y3, x1, y1)
Perimeter = (a + b + c)
S =abs((x1-x3)*(y2-y3)-(x2-x3)*(y1-y3))/2
print(round(Perimeter,5), S)