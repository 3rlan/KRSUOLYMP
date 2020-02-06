import random
n, x = map(int, input().split())
aList = [random.choice([i for i in range(0, 6)]) for j in range(n)]
indices = [i for i, target in enumerate(aList) if target == x]
print(aList)
for i in indices:
    print(i)