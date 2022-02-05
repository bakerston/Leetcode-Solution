# Biweekly Contest 71  


完成4题，用时 58:31\
6次错误，总成绩1:28:31\
[排名 **518/16927**](https://leetcode.com/contest/weekly-contest-274/ranking/4/)\
死了妈了第三题
  
  
## [2160. Minimum Sum of Four Digit Number After Splitting Digits](https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/)

> 贪心法，把非零数字从小到大排序，依次分配给A,B两个数。
> 比如001234，A就是13，B是24.

#### Python
```swift
def minimumSum(self, num: int) -> int:
        s = sorted(str(num))
        a, b = "", ""
        i, idx, n = 0, 0, len(s)
        while idx < n:
            if i % 2:
                a += s[idx]
            else:
                b += s[idx]
            i += 1
            idx += 1
        return int(a) + int(b)
```
  
  
## [2161. Partition Array According to Given Pivot](https://leetcode.com/problems/partition-array-according-to-given-pivot/)

> 三个空数组A,B,C，遍历数组，比pivot小的放在A，等于pivot的放在B，大于pivot的放在C。 
> 返回A+B+C.

#### Python
```swift
def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        return [x for x in nums if x < pivot] + [x for x in nums if x == pivot] + [x for x in nums if x > pivot]
```
  
  

## [2162. Minimum Cost to Set Cooking Time](https://leetcode.com/problems/rearrange-array-elements-by-sign/)

> 草泥马的沙比问题\
> [我的LeetCode题解](https://leetcode.com/problems/minimum-cost-to-set-cooking-time/discuss/1747222/Python-Be-careful-with-some-annoying-edge-cases.)

#### Python
```swift
def minCostSetTime(self, start: int, mC: int, pC: int, TS: int) -> int:
        def helper(mins, secs):
            pre, cost, ss = str(start), 0, str(secs)
            if mins != 0:
                if len(ss) < 2:
                    ss = "0" + ss
                ss = str(mins) + ss            
            for ch in ss:
                if ch != pre:
                    cost += mC
                cost += pC
                pre = ch
            return cost

        mins, secs = divmod(TS, 60)
        ans = math.inf
        
        if mins < 100:
            ans = min(ans, helper(mins, secs))
        if secs < 40:
            ans = min(ans, helper(mins - 1, secs + 60))
        return ans
```

## [2163. Minimum Difference in Sums After Removal of Elements](https://leetcode.com/problems/find-all-lonely-numbers-in-the-array/)


> [我的LeetCode题解](https://leetcode.com/problems/minimum-cost-to-set-cooking-time/discuss/1747222/Python-Be-careful-with-some-annoying-edge-cases.)\
> 思路类似找prefix和suffix。\
> 假设原数组长度为**3n**，我们需要找出长度均为n的两个子数组（假设为A和B，A在B前），使得sum(A)-sum(B)最小。\
> 我们把原数组分为两部分，从这两部分里找出A和B来，显然，两部分的长度都要大于等于**n**。\
> 好的，现在问题变成了，我们要从A中找出最小的n个数，从B中找出最大的n个数来。这样才有可能保证sum(A)-sum(B)最小。\
> 有多少种分法呢？一共是n+1种，（A=n,B=2n),(A=n+1,B=2n-1), ... , (A=2n,B=n)\
> 对于每一种分法，我们可以通过排序，找出各自部分中最小（大）的**n**个数，时间复杂度为O(N^2 logN)，很慢\
> 我们可以观察到，其实A或者B，在相邻的两种分法之间，只是差了一个数，所以如果我们能维持一个长度为n的最小（大）堆\
> 每次遇到新的数后，把这个数插入堆中并弹出所有数种最小（大）数来，这样只需要O(logN)的时间，就能完成一个新的分法的排序\
> 总时间复杂度O(N logN)\
> 说不清楚了，越说越乱，球球看我的题解吧。

#### Python
```swift
def minimumDifference(self, A: List[int]) -> int:
        n = len(A) // 3
        
        # Build pre_min using min-heap.
        pre_min, cur_min = [sum(A[:n])], sum(A[:n])
        pre_hp = [-x for x in A[:n]]
        heapq.heapify(pre_hp)
        for i in range(n, 2 * n):
            cur_pop = -heapq.heappop(pre_hp)
            cur_min -= cur_pop
            cur_min += min(cur_pop, A[i])
            pre_min.append(cur_min)
            heapq.heappush(pre_hp, -min(cur_pop, A[i]))          
        
        # Build suf_max.
        suf_max, cur_max = [sum(A[2*n:])], sum(A[2*n:])
        suf_hp = [x for x in A[2*n:]]
        heapq.heapify(suf_hp)        
        for i in range(2 * n - 1, n - 1, -1):
            cur_pop = heapq.heappop(suf_hp)
            cur_max -= cur_pop
            cur_max += max(cur_pop, A[i])
            suf_max.append(cur_max)
            heapq.heappush(suf_hp, max(cur_pop, A[i]))
        suf_max = suf_max[::-1]
        
        # Iterate over pre_min and suf_max and get the minimum difference.
        ans = math.inf
        for a, b in zip(pre_min, suf_max):
            ans = min(ans, a - b)
        return ans 
```

