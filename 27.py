from itertools import combinations, permutations

n, s = map(int, input().split(" "))
numbers = list(map(int, input().split(" ")))

result = -1

for triplet in combinations(numbers, 3):
    if sum(triplet) != s:
        continue
    for combination in permutations(triplet): # (1, 2, 3), 123
        if combination[0] == 0:
            continue
        number = combination[0] * 100 + combination[1] * 10 + combination[2]
        if number < result or result == -1:
            result = number

print(result)