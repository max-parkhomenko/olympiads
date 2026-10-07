from itertools import combinations, permutations
n, s = map(int, input().split())
values = list(map(int, input().split()))

result = 0
for comb in combinations(values, 3):
    