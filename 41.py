n, q = map(int, input().split())
allowed = list(map(int, input().split()))
requests = list(map(int, input().split()))

for req in requests:
    if req in allowed:
        print("YES")
    else:
        print("NO")