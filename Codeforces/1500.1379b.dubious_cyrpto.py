n = int(input())
for _ in range(n):
    l, r, m = list(map(int, input().split()))
    lft, rgt = m + l - r - 1, m + r - l
    for i in range(l, r + 1):
        if lft // i != rgt // i:
            n = rgt // i
            dif = m - n * i
            if dif > 0:
                print(i, l + dif, l)
            elif dif < 0:
                print(i, r + dif, r)
            else:
                print(i, l, l)
            break
