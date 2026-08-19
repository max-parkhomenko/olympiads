n, s = map(int, input().split())
scores = list(map(int, input().split()))

result = 0

for i in range(n):
    first = scores[i]
    for j in range(i + 1, n):
        second = scores[j]
        if first + second == s:
            result += 1

print(result)