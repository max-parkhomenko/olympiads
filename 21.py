s = int(input())

result = 0

for i in range(10):
    for j in range(10):
        if i + j != s:
            continue
        if i < j:
            result += 1

print(result)
