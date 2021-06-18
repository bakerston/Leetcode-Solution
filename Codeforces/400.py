"""x = input()
if int(x) > 2 and int(x) % 2 == 0:
    print("YES")
else:
    print("NO")"""


#A. Domino piling
n, s = map(int, input().split(" "))
print((n * s) // 2)