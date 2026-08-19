h, m = map(int, input().split(" "))

minutes = h * 60 + m
minutes_to_midnight = 1440 - minutes
print(minutes)
print(minutes_to_midnight)
