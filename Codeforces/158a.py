n, s = map(int, input().split(" "))
p = input().split(" ")
ans = 0
cur = int(p[s - 1])
for x in p:
    if int(x) >= cur and int(x) > 0:
        ans += 1
print(ans)