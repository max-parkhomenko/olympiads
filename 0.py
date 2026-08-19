n, a, b = map(int, input().split(" "))

result = 0

for i in range(n+1):
    if i % a == 0 and i % b != 0:
        result += 1


print(result)
