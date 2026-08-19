h, m, x, y = map(int, input().split(" "))
commands = input()

start_minutes = h * 60 + m
end_minutes = (start_minutes + len(commands)) % 1440

for command in commands:
    match command:
        case "N":
            y += 1
        case "S":
            y -= 1
        case "E":
            x += 1
        case "W":
            x -= 1

hours = end_minutes // 60
minutes = end_minutes % 60
print(x, y)
print(f"{hours:02d}:{minutes:02d}")
