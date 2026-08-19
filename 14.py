n, fuel = map(int, input().split(" "))
needs = list(map(int, input().split(" ")))

i = 0
while i < n and needs[i] <= fuel:
    fuel -= needs[i]
    i += 1

print(i)
print(fuel)
