n = int(input())
l = list(map(int, input().split()))

first = 0
second = 0

for i in range(n):
    if l[i] > first:
        second = first
        first = l[i]
    elif l[i] > second:
        second = l[i]

print(first + second)