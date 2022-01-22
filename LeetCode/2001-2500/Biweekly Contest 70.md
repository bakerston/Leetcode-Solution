# Biweekly Contest 70  

完成4题，用时24：36\
两次错误，总成绩34：36\
[排名 **58/17655**](https://leetcode.com/contest/biweekly-contest-70/ranking/3/)

## [2144. Minimum Cost of Buying Candies With Discount](https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/)

> 贪心法，商品按照价格倒序排序（从高到低），每购买两个商品，可以免费获得第三个。
> 
> [付费][付费][免费] [付费][付费][免费] ...
> 
> 最后，加上剩下的凑不够3个的商品。比如5个商品，最后会剩下两个价格最低的，全部是付费的。

#### **Python**
```swift
def minimumCost(self, A: List[int]) -> int:
        A.sort(reverse = True)
        n, ans = len(A), 0
        for i in range(n // 3):
            ans += A[3 * i] + A[3 * i + 1]
        res = n % 3

        return ans if n % 3 == 0 else ans + sum(A[-(n % 3):])
```

## [2145. Count the Hidden Sequences](https://leetcode.com/problems/count-the-hidden-sequences/)

> 算出数组A上下界的差值，如果差值大于upper-lower，则不存在数组。
> 

#### Python
```swift
def numberOfArrays(self, A: List[int], lower: int, upper: int) -> int:
        acc = [0] + list(itertools.accumulate(A))
        lo, up = min(acc), max(acc)
        if up - lo > upper - lower:
            return 0
        return upper - lower - (up - lo) + 1
```

## [2146. K Highest Ranked Items Within a Price Range](https://leetcode.com/problems/k-highest-ranked-items-within-a-price-range/)

> [LeetCode 题解](https://leetcode.com/problems/k-highest-ranked-items-within-a-price-range/discuss/1709722/Explanation-with-pictures-BFS)\
> BFS法，从出发点开始，搜索所有**未被访问**的邻居（这个邻居可以是商品，也可以是empty cell），记录下该邻居与出发点的距离。\
> 如果某个商品的值介于price之间，说明这个商品**有可能**是答案之一，我们把它放到备选列表里\
> 因为最终选定前**K**个商品要参考四个条件:距离，价格，行数，列数。所以我们储存每一个备选商品时，储存的就是这四个条件。([距离，价格，行数，列数])\
> 遍历完所有可能的商品后，按照上述四个条件，对备选商品列表排序，取出前**K**个的坐标值即可

#### Python
```swift
def highestRankedKItems(self, A: List[List[int]], price: List[int], start: List[int], k: int) -> List[List[int]]:
        ans = []
        dq = collections.deque([(start[0], start[1], 0)])
        seen = set([(start[0], start[1])])
        
        dirs = ((1, 0), (0, 1), (-1, 0), (0, -1))
        m, n = len(A), len(A[0])

        while dq:
            cx, cy, dist = dq.popleft()
            if price[0] <= A[cx][cy] <= price[1]:
                ans.append([dist, A[cx][cy], cx, cy])
            for dx, dy in dirs:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in seen and A[nx][ny] > 0:
                    seen.add((nx, ny))
                    dq.append((nx, ny, dist + 1))
                    
        ans.sort()
        
        return [x[2:] for x in ans[:k]]
```

## [2147. Number of Ways to Divide a Long Corridor](https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/)

> 贪心法，算出每**两个**沙发之间有多少植物，有N颗植物，代表着有N+1钟插板方法。\
> 连乘所有插板方法数量，取1E9+7的余即可\
> 如果没有沙发，或者沙发的数量是奇数，说明没有方法可以分割房间，返回0。

#### Python
```swift
def numberOfWays(self, A: str) -> int:
        c = collections.Counter(A)
        if c['S'] == 0 or c['S'] % 2: 
            return 0

        pos = [i for i, x in enumerate(A) if x == 'S']
        room, cur, mod = len(pos) // 2, 1, 10 ** 9 + 7

        for i in range(room - 1):
            cur *= (pos[2 * i + 2] - pos[2 * i + 1])
            cur %= mod
        return cur
```
