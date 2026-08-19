t, n = map(int, input().split(" "))
capacity, fuel, refill = map(int, input().split(" "))
needs = list(map(int, input().split(" ")))

i = 0
ships = 0
while i < t and ships < n:
    next_fuel = fuel + refill
    fuel = min(next_fuel, capacity)
    if needs[ships] <= fuel:
        fuel -= needs[ships]
        ships += 1
    i += 1

print(ships)
print(fuel)
