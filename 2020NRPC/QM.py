import sys
import collections
import collections
line1 = sys.stdin.readline().strip()
line2 = sys.stdin.readline().strip()
c1 = collections.Counter(line1)
c2 = collections.Counter(line2)
if c1["S"] == 0 or c2["S"] == 0:
    print(0)
else:
    k = c1["S"] * c2["S"]
    for i in range(k):
        print("S(", end = "")
    print("0", end = "")
    for i in range(k):
        print(")", end = "")

