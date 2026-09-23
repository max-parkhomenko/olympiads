x, n = map(int, input().split())

while n > 0:
    n -= 1
    if x % 2 == 0:
        x += 3
    else:
        x -= 1

print(x)