commands = input()

x = 0
y = 0

for c in commands:
    match c:
        case "U":
            y += 1
        case "D":
            y -= 1
        case "L":
            x -= 1
        case "R":
            x += 1

print(x, y, abs(x) + abs(y))