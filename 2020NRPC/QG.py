import sys

a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()

nums = list(map(int, b.split()))

ans = 0
num = 0
cur = 0
for n in nums:
    if n == 3:
        ans += cur
        ans %= 10 ** 9 + 7
    elif n == 2:
        cur = ((cur + num) * 2 - num) % (10 ** 9 + 7)
    else:
        num += 1
print(ans % (10 ** 9 + 7))

