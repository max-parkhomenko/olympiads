import time

s = int(input())

result = 0
start = time.perf_counter()
for i in range(10):
    for j in range(10):
        for k in range(10):
            if i + j + k != s:
                continue
            if i < j < k:
                result += 1

end = time.perf_counter()
print(result)
print(end - start)
