import sys
a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()

alen = len(a)
blen = len(b)
s = min(alen, blen)
find = False
for idx in range(-s, 0, 1):
    cur = int(a[idx]) + int(b[idx])
    if cur >= 10:
        s = max(a[idx:], b[idx:])
        n = len(s)
        carry = 0
        ans = ""
        for i in s[::-1]:
            if int(i) + carry == 0:
                ans += "0"
                carry = 0
            else:
                ans += str(10 - int(i) - carry)
                carry = 1      
        leading = True
        res =""
        for i in ans[::-1]:
            if leading:
                if i != "0":
                    res += i
                    leading = False
            else:
                res += i
        print(res)
        find = True
        break
if not find:
    print("0")