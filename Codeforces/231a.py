n = int(input())
ans = 0
for _ in range(n):
    s = input()
    s = map(int, s.split(" "))
    if sum(s) > 1:
        ans += 1
print(ans)