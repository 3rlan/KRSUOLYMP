s = input()
temp = ''
for i in s:
    temp += i + ", "

print(temp[0: len(temp) - 2])