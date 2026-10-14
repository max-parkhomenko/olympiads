n = int(input())
ll = list(map(int, input().split()))
counted = {}

for i in ll:
    counted[i] = counted.get(i, 0) + 1

print(max(counted.values()))