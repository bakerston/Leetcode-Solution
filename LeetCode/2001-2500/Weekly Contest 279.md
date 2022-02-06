# Weekly Contest 279  

完成4题，用时53:23\
3次错误，总成绩1:08:23\
[排名 **468/18838**](https://leetcode.com/contest/weekly-contest-279/ranking)

## [2164. Sort Even and Odd Indices Independently](https://leetcode.com/problems/sort-even-and-odd-indices-independently/)

> 数组切片，正序、倒序排列。

#### **Python**
```swift
def sortEvenOdd(self, A):
        A[::2], A[1::2] = sorted(A[::2]), sorted(A[1::2])[::-1]
        return A
```

## [2165. Smallest Value of the Rearranged Number](https://leetcode.com/problems/smallest-value-of-the-rearranged-number/)

> - 如果num是0，直接返回0
> - 如果num大于0，把num所有数字从小到大排序，把第一个非零数换到在首位，比如000123换成100023.
> - 如果num小于0，把num所有数字从大到小排序，输出该数（加负号）即可，比如-12304换成-43210

#### Python
```swift
def smallestNumber(self, num: int) -> int:
        if num == 0: return 0
        pos = num > 0
        A = list(str(abs(num)))
        n = len(A)
        if pos:
            A.sort()
            idx = 0
            while idx < n and A[idx] == '0':
                idx += 1
            A[0], A[idx] = A[idx], A[0]
        else:
            A.sort(reverse = True)
        curr = int("".join(A))
        return curr if pos else -curr
```

## [2166. Design Bitset](https://leetcode.com/problems/design-bitset/)

> 一些比较基础的bitwise operation

#### Python
```swift
class Bitset:

    def __init__(self, size: int):
        self.size = size
        self.n = 0
        self.full = 1 << size

    def fix(self, idx: int) -> None:
        self.n |= 1 << (self.size - idx - 1)

    def unfix(self, idx: int) -> None:
        mask = 1 << (self.size - idx - 1)
        self.n &= ~mask

    def flip(self) -> None:
        self.n ^= (self.full - 1)

    def all(self) -> bool:
        return self.n + 1 == self.full

    def one(self) -> bool:
        return self.n != 0

    def count(self) -> int:
        return self.n.bit_count()
    
    def toString(self) -> str:
        n = bin(self.n)[2:]
        return "0" * (self.size - len(n)) + n
```

## [2167. Minimum Time to Remove All Cars Containing Illegal Goods](https://leetcode.com/problems/minimum-time-to-remove-all-cars-containing-illegal-goods/)

> [我的LeetCode题解](https://leetcode.com/problems/minimum-time-to-remove-all-cars-containing-illegal-goods/discuss/1748452/Python-Explanation-with-pictures.-Prefix-and-Suffix.)
> 
> 抛砖引玉，大家可以重点看下Discuss前两位大佬的解法，比我这种left-right DP要简单得多。\
> 他们的思路类似Kadane算法：一次遍历得到最大子序列的和。


#### Python

```swift
def minimumTime(self, A: str) -> int:
        n = len(A)
        if n == 1: return 1 if A == '1' else 0
        lft, rgt = [] * n, [] * n
        
        curr = 0
        for a in A:
            if a == '1':
                curr += 1
            else:
                curr -= 1
            lft.append(curr)
            
        curr = 0
        for a in A[::-1]:
            if a == '1':
                curr += 1
            else:
                curr -= 1
            rgt.append(curr)
        rgt.reverse()

        exp = 2 * A.count('1')   # MaximumCost, that is the cost of removing all cars with a cost of 2.
            
        lmax, curr = [lft[0]], lft[0]
        for i in range(1, n):
            curr = max(curr, lft[i])
            lmax.append(curr)
            
        rmax, curr = [rgt[-1]], rgt[-1]
        for i in range(n - 2, -1, -1):
            curr = max(curr, rgt[i])
            rmax.append(curr)            
        rmax.reverse()
        
        maxp = 0  # The maximum cost we can SAVE.
        for i in range(n - 1):
            maxp = max(maxp, max(0, lmax[i]) + max(0, rmax[i + 1]))

        return exp - maxp  # The overall cost is the MaximumCost - "the maximum cost we can save".
```
