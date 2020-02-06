import random
import operator
n = int(input())
a = []
for x in range(n):
    a.append(random.randint(-100, 100))
print(*a, sep=" ")

max_index, max_value = max(enumerate(a), key=operator.itemgetter(1))
min_index, min_value = min(enumerate(a), key=operator.itemgetter(1))
print(min_value,min_index)
print(max_value,max_index)