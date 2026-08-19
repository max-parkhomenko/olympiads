start_h, start_m, end_h, end_m = map(int, input().split(" "))

start_minutes = start_h * 60 + start_m
end_minutes = end_h * 60 + end_m

# 23:50 - 1430
# 00:17 - 17
if end_minutes < start_minutes:
    print(1440 - start_minutes + end_minutes)
else:
    print(end_minutes - start_minutes)
