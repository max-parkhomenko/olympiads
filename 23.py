s, k = map(int, input().split(" "))

result = -1

for i in range(100, 999):
    i_list = [int(str(i)[0]), int(str(i)[1]), int(str(i)[2])]
    if not i_list[0] != i_list[1] != i_list[2]:
        continue
    if sum(i_list) != s:
        continue
    if i % k != 0:
        continue
    result = i
    break

print(result)
