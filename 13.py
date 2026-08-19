start, charge, target = map(int, input().split(" "))

minutes = 0

while start < target:
    start += charge
    minutes += 1

print(minutes)
print(start)
