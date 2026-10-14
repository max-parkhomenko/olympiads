n = int(input())
ll = list(map(int, input().split()))
onetime = set()
moretimes = set()

for i in ll:
    if i not in onetime:
        if i not in moretimes:
            onetime.add(i)
    else:
        onetime.remove(i)
        moretimes.add(i)

print(len(onetime))