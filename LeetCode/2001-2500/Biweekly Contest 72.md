# Biweekly Contest 72  


完成4题，用时 25:38\
0次错误，总成绩 25:38\
[排名 **45/14241**](https://leetcode.com/contest/biweekly-contest-72/ranking/2/)
  
  
## [2176. Count Equal and Divisible Pairs in an Array](https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/)

> 数组很小，暴力求解，检查每个下标对（i，j）是否符合要求。

#### Python
```python3
def countPairs(self, A: List[int], k: int) -> int:
        ans, n = 0, len(A)
        for i in range(n - 1):
            for j in range(i + 1, n):
                ans += int(A[i] == A[j] and not (i * j) % k):
        return ans
```
  
  
## [2177. Find Three Consecutive Integers That Sum to a Given Number](https://leetcode.com/problems/find-three-consecutive-integers-that-sum-to-a-given-number/)

> 检查是`num`是否被3整除。

#### Python
```python3
def sumOfThree(self, num: int) -> List[int]:
        return [] if num % 3 else [num // 3 - 1, num //3, num // 3 + 1]
```
  
  

## [2178. Maximum Split of Positive Even Integers](https://leetcode.com/problems/maximum-split-of-positive-even-integers/)


> 先检查A是否是偶数，如果是奇数返回[]  
> 贪心法，最开始的数组是[]  
> 从最小的正偶数2开始，如果 2 加上之前数组之和依旧小于等于A，说明2可以放到数组里。  
> 把2放到数组里，用下一个偶数4重复上一步：如果 4 加上 之前数组之和依旧小于等于A， 说明4也可以放到数组里。
> 直到某个偶数加上之前数组和大于A，这个数是不能放到数组里了。把A-sum(数组)加到数组中最大的偶数上即可。
> 

#### Python
```swift
def maximumEvenSplit(self, A: int) -> List[int]:
      if A % 2: return []
      ans, cur, A = [2], 4, A - 2
      while A >= cur:
          ans.append(cur)
          A -= cur
          cur += 2
      ans[-1] += A
      return ans
```

## [2179. Count Good Triplets in an Array](https://leetcode.com/problems/count-good-triplets-in-an-array/)


> [我的LeetCode题解](https://leetcode.com/problems/count-good-triplets-in-an-array/discuss/1783205/Python-Explanation-with-pictures.-O(N-logN)-Time.)
> 
> 思路是：只看triplet里中间的那个数：
> 对于每一个数a，我们需要找到：以a为中心的triplet有多少？这样，把所有数的triplets加一起即可。
> 所以，对于数a我们需要找到：
> - 有多少数，它们在A,B里位置均在a的左边，比如有x个数。
> - 有多少数，它们在A,B里的位置均在a的右边，比如有y个数。
> - 那么，以a为中心的triple共有x* y种。
> 
> 遍历过程需要logN时间内的插入/二分查找，数据结构用BST或者BIT都可以。我用的是Python有现成的BST容器SortedList。

#### Python
```python3
from sortedcontainers import SortedList
class Solution:
    def goodTriplets(self, A: List[int], B: List[int]) -> int:
        # Index of a (from A) in B.
        pos = [0] * len(A)               
        for idx, b in enumerate(B):
            pos[b] = idx
        
        # Build pre_a[i]: number of elements on a[i]'s left in both A and B.
        # pos_in_b: sorted indexes (in B) of all the visited elements in A.
        pos_in_b, pre_a = SortedList([pos[A[0]]]), [0]      
        for a in A[1:]:       
            pos_in_b.add(pos[a])
            pre_a.append(pos_in_b.bisect_left(pos[a]))
    
        # Build suf_a[i]: number of elements on a[i]'s right in both A and B.
        pos_in_b, suf_a = SortedList([pos[A[-1]]]), [0]
        for a in reversed(A[:len(A)-1]):
            idx = pos_in_b.bisect(pos[a])
            suf_a.append(len(pos_in_b) - idx)
            pos_in_b.add(pos[a])
        suf_a.reverse()
        
        # Sum up all unique triplets centered on A[i].
        ans = 0
        for x, y in zip(pre_a, suf_a):
            ans += x * y
        return ans
```
