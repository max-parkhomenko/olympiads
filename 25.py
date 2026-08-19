from itertools import combinations

n, s = map(int, input().split(" "))
prices = list(map(int, input().split(" ")))

result = 0

for trio in combinations(prices, 3):
    if sum(trio) == s:
        result += 1

print(result)