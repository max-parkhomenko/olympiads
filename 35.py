n = int(input())
l = list(map(int, input().split()))

result = 0

for i in range(1, n):
    if l[i] > l[i - 1]:
        result += 1

print(result)