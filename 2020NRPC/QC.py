import sys
import heapq
a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()

nums = list(map(int, b.split()))
m = sum(nums)
maxi = max(nums)
if m % 2 or 2 * maxi > m:
    print("no")
else:
    print("yes")
    res = []
    for i, n in enumerate(nums):
        heapq.heappush(res, [-n, i])
    while m > 0:
        p = heapq.heappop(res)
        q = heapq.heappop(res)
        print(p[1] + 1," ",q[1] + 1)
        p[0] += 1
        q[0] += 1
        if p[0] < 0:
            heapq.heappush(res, p)
        if q[0] < 0:
            heapq.heappush(res, q)  
        m -= 2




