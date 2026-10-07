n = int(input())
codes = set(map(int, input().split()))

print(n - len(codes))