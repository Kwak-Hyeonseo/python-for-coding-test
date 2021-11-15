data = list(input())
data.sort()
total = 0
for i in data:
    if i.isdigit():
        total += int(i)
    else:
        print(i, end='')
print(total)
