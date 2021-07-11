a = input().lower()
b = input().lower()
n, ans = len(a), 0
for i in range(n):
    if b[i] > a[i]:
        ans -= 1
    elif b[i] < a[i]:
        ans += 1
print(ans)
