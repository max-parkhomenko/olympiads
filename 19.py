x1, y1, x2, y2 = map(int, input().split(" "))

steps_x = abs(x2 - x1)
steps_y = abs(y2 - y1)

print(steps_x + steps_y)
