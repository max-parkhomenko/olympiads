n, capacity, cargo = map(int, input().split(" "))
changes = list(map(int, input().split(" ")))

cancels = 0
for change in changes:
    next_cargo = cargo + change
    if 0 <= next_cargo <= capacity:
        cargo = next_cargo
    else:
        cancels += 1

print(cargo)
print(cancels)
