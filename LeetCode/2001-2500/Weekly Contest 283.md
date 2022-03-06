# Weekly Contest 283 

完成4题，用时44：19\
0次错误，总成绩44：19\
[排名 **252/21847**](https://leetcode.com/contest/weekly-contest-283/ranking/11/)

## [2194. Cells in a Range on an Excel Sheet](https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet/)

> 按行+列遍历

<details>
    <summary> Python </summary>   
  
```python
def cellsInRange(self, s: str) -> List[str]:
        start_col, end_col = s[0], s[3]
        start_row, end_row = int(s[1]), int(s[4])
        ans = []
        for i in range(ord(start_col), ord(end_col) + 1):
            for j in range(start_row, end_row + 1):
                ans.append(chr(i) + str(j))
        return ans
```
</details>


## [2195. Append K Integers With Minimal Sum](https://leetcode.com/problems/append-k-integers-with-minimal-sum/)

> [我的LeetCode题解](https://leetcode.com/problems/append-k-integers-with-minimal-sum/discuss/1823621/Python-Explanation-with-pictures-Binary-Search)\
> 二分法，找最后一个integer需要插入的位置。
> 
![283-1](https://user-images.githubusercontent.com/38169559/156909048-7de49ab1-344a-487a-bc40-4fea6f803b73.png)
![283-2](https://user-images.githubusercontent.com/38169559/156909063-ab19cf78-4b9b-4726-8d44-d3ac2a561681.png)

遍历可以找出最后一个integer的位置，但需要线性时间。

![283-3](https://user-images.githubusercontent.com/38169559/156909065-30f7a171-91e1-48ec-8b4b-ffe73eacab95.png)
二分法，对数时间。

![283-4](https://user-images.githubusercontent.com/38169559/156909067-d544ecad-9031-42dc-a10b-6ba0e2bc5657.png)

<details>
    <summary> Python </summary>   
  
```python
def minimalKSum(self, nums: List[int], k: int) -> int:
        nums = sorted(list(set(nums)))
        n = len(nums)   
        if nums[n - 1] <= k + n:
            return (k + n) * (k + n + 1) // 2 - sum(nums)

        lft, rgt = 0, n - 1
        while rgt > lft:
            mid = (lft + rgt) // 2
            if nums[mid] - mid <= k:
                lft = mid + 1
            else:
                rgt = mid
        return (k + lft + 1) * (k + lft) // 2 - sum(nums[:lft])                                 
```
                                   
</details>

## [2196. Create Binary Tree From Descriptions](https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/)

> BFS
> 建立每个节点之间的关系，把root加入FIFO队列。
> 弹出当前队列，检查它有无左右子节点，如果有的话，建立相应关系，并把相应子节点也加入队列。

<details>
    <summary> Python </summary>   

```python
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, A: List[List[int]]) -> Optional[TreeNode]:
        lc, rc, p = collections.defaultdict(int), collections.defaultdict(int), collections.defaultdict(int)
        al, rootval = set(), -1
        for pp, cc, ss in A:
            p[cc] = pp
            if ss == 1:
                lc[pp] = cc
            else:
                rc[pp] = cc
            al.add(pp)
            al.add(cc)
        
        for a in al:
            if a not in p:
                rootval = a
                break
                
        root = TreeNode(rootval)
        dq = collections.deque()
        dq.append(root)
        dummy = TreeNode(val=None, left=root)
        while dq:
            curr = dq.popleft()
            if curr.val in lc:
                lft = TreeNode(lc[curr.val])
                curr.left = lft
                dq.append(lft)
            if curr.val in rc:
                rgt = TreeNode(rc[curr.val])
                curr.right = rgt
                dq.append(rgt)
        return dummy.left
```
  
</details>

## [2197. Replace Non-Coprime Numbers in Array](https://leetcode.com/problems/replace-non-coprime-numbers-in-array/)

> 优先队列

<details>
    <summary> Python </summary>   
  
```python
def replaceNonCoprimes(self, s: List[int]) -> List[int]:
        st = []
        for num in s:
            while st and math.gcd(st[-1], num) > 1:
                num = math.lcm(num, st.pop())
            st.append(num)
        return st

```
</details>

