from itertools import permutations

n, d = map(int, input().split(" "))
levels = list(map(int, input().split(" ")))

result = 0

for combination in permutations(levels):
    playlist = True
    for i in range(n - 1): # [1, 2, 3, 4, 5]
        first = combination[i]
        second = combination[i + 1]
        if abs(first - second) > d:
            playlist = False
            break
    if playlist:
        result += 1

print(result)