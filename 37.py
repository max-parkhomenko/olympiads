n = int(input())
l = list(map(int, input().split()))

result = 0

for i in range(2, n):
    if l[i-2] < l[i - 1] > l[i]:
        result += 1

print(result)