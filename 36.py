n = int(input())
l = list(map(int, input().split()))

current = 1
current_n = 0
maximum = 1

for i in range(n):
    if l[i] == current_n:
        current += 1
    else:
        current = 1
    current_n = l[i]
    if maximum < current:
        maximum = current


print(maximum)