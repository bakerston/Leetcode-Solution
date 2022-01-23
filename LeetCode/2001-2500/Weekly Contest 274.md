# Weekly Contest 274  

完成4题，用时1:08:23\
0次错误，总成绩1:08:23\
[排名 **76/14086**](https://leetcode.com/contest/weekly-contest-274/ranking/4/)

## [2124. Check if All A's Appears Before All B's](https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/)

> 检查字符串中有没有'ba'

#### **Python**
```swift
def checkString(self, s: str) -> bool:
        find = False
        for ch in s:
            if ch == 'b':
                find = True
            else:
                if find:
                    return False
        return True
```

## [2125. Number of Laser Beams in a Bank](https://leetcode.com/problems/number-of-laser-beams-in-a-bank/)

> 计算相邻两层中laser数量的乘积，连乘。


#### Python
```swift
def numberOfBeams(self, A: List[str]) -> int:
        ans = []
        for row in A:
            c = collections.Counter(row)
            if c['1'] > 0:
                ans.append(c['1'])
        if len(ans) < 2: return 0
        res = 0
        for i in range(len(ans) - 1):
            res += ans[i] * ans[i + 1]
        return res
```

## [2126. Destroying Asteroids](https://leetcode.com/problems/destroying-asteroids/)

> 数组排序，依次对比mass质量与排序后的数组元素大小。

#### Python
```swift
def asteroidsDestroyed(self, mass: int, A: List[int]) -> bool:
        A.sort()
        for a in A:
            if mass < a:
                return False
            mass += a
        return True
```

## [2127. Maximum Employees to Be Invited to a Meeting](https://leetcode.com/problems/maximum-employees-to-be-invited-to-a-meeting/)

> [LeetCode题解](https://leetcode.com/problems/maximum-employees-to-be-invited-to-a-meeting/discuss/1661178/Explanation-with-pictures.)\
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
