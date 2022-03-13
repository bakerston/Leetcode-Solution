# Weekly Contest 284 

完成4题，用时1:09:39\
0次错误，总成绩1:09:39\
[排名 **299/25676**](https://leetcode.com/contest/weekly-contest-284/ranking/4/)

## [2200. Find All K-Distant Indices in an Array](https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/)

> 找所有符合的index，把左右范围内所有下标都加到集合中取并集。

<details>
    <summary> Python </summary>   
  
```python
def findKDistantIndices(self, A: List[int], key: int, k: int) -> List[int]:
        ans = set()
        for i, x in enumerate(A):
            if x == key:
                ans.add(i)
        tmp = set()
        n = len(A)
        for a in ans:
            for i in range(a - k, a + k + 1):
                if 0 <= i < n:
                    tmp.add(i)
        return sorted(list(tmp))
```
</details>


## [2201. Count Artifacts That Can Be Extracted](https://leetcode.com/problems/count-artifacts-that-can-be-extracted/)

> hashset，先把每个宝藏X的每块地板编号。\
> 每挖一块地板，看这个地板下的宝藏（如果有的话）属于第几号宝藏，如果该宝藏的每一块地板都被挖过了\
> 答案加一。

<details>
    <summary> Python </summary>   
  
```python
def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        pos = collections.defaultdict(int)
        cnt = collections.defaultdict(int)
        ans = 0
        for i, a in enumerate(artifacts):
            x1, y1, x2, y2 = a
            cnt[i] = (x2 - x1 + 1) * (y2 - y1 + 1)
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    pos[(x, y)] = i
        for x, y in dig:
            if (x, y) in pos:
                curr = pos[(x, y)]
                if cnt[curr] == 1:
                    ans += 1
                cnt[curr] -= 1
        return ans)                                 
```
                                   
</details>

## [2202. Maximize the Topmost Element After K Moves](https://leetcode.com/problems/maximize-the-topmost-element-after-k-moves/)

> PriorityQueue, 把数组中的数，按照【数值由大到小】+【坐标由小到大】排序\
> 对于堆顶的每个数，考虑是否可以用K次操作把这个数置顶。

<details>
    <summary> Python </summary>   

```python
def maximumTop(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pq = []
        if n == 1:
            return nums[0] if k % 2 == 0 else -1
        for i, num in enumerate(nums):
            heapq.heappush(pq, (-num, i))

        while pq:
            cur, idx = heapq.heappop(pq)
            if idx > k:
                continue
            elif idx == k:
                return -cur
            else:
                res = k - idx
                if res == 1:
                    continue 
                else:
                    return -cur
        return -1
```
  
</details>

## [2203. Minimum Weighted Subgraph With the Required Paths](https://leetcode.com/problems/replace-non-coprime-numbers-in-array/)

> [我的LeetCode题解](https://leetcode.com/problems/minimum-weighted-subgraph-with-the-required-paths/discuss/1844113/Python-Explanation-with-pictures-Dijkstra)\
> Dijkstra

<details>
    <summary> Python </summary>   
  
```python
def minimumWeight(self, n: int, E: List[List[int]], s1: int, s2: int, d: int) -> int:
        d1, d2, dd = [math.inf] * n, [math.inf] * n, [math.inf] * n
        d1[s1] = d2[s2] = dd[d] = 0
        nxxt, prev = collections.defaultdict(dict), collections.defaultdict(dict)
        ans = math.inf
        for s, e, w in E:
            nxxt[s][e] = min(nxxt[s].get(e, math.inf), w)
            prev[e][s] = min(prev[e].get(s, math.inf), w)

        pq, visited = [], set([s1])
        for nxt in nxxt[s1]:
            heapq.heappush(pq, [nxxt[s1][nxt], nxt])
        while pq:
            curw, curn = heapq.heappop(pq)
            if curn not in visited:
                visited.add(curn)
                d1[curn] = min(d1[curn], curw)
                for nxt in nxxt[curn]:
                    heapq.heappush(pq, [nxxt[curn][nxt] + curw, nxt])

        pq, visited = [], set([s2])
        for nxt in nxxt[s2]:
            heapq.heappush(pq, [nxxt[s2][nxt], nxt])
        while pq:
            curw, curn = heapq.heappop(pq)
            if curn not in visited:
                visited.add(curn)
                d2[curn] = min(d2[curn], curw)
                for nxt in nxxt[curn]:
                    heapq.heappush(pq, [nxxt[curn][nxt] + curw, nxt])

        pq, visited = [], set([d])
        for pre in prev[d]:
            heapq.heappush(pq, [prev[d][pre], pre])
        while pq:
            curw, curn = heapq.heappop(pq)
            if curn not in visited:
                visited.add(curn)
                dd[curn] = min(dd[curn], curw)
                for pre in prev[curn]:
                    heapq.heappush(pq, [prev[curn][pre] + curw, pre])
                    
        for i, w in enumerate(dd):
            if d1[i] == math.inf or d2[i] == math.inf:
                continue
            ans = min(ans, dd[i] + d1[i] + d2[i])
        return ans if ans < math.inf else -1

```
</details>
