# Biweekly Contest 73 

完成4题，用时39：05\
0次错误，总成绩39：05\
[排名 **110/18529**](https://leetcode.com/contest/biweekly-contest-73/ranking/5/)

## [2190. Most Frequent Number Following Key In an Array](https://leetcode.com/problems/most-frequent-number-following-key-in-an-array/)

> 统计频率


<details>
    <summary> Python </summary>   
  
```python
def mostFrequent(self, A: List[int], key: int) -> int:
        freq = collections.defaultdict(int)
        n = len(A)
        for i in range(1, n):
            if A[i - 1] == key:
                freq[A[i]] += 1
        c = max(freq.values())
        ans = 0
        print(freq)
        for x in list(freq.keys()):
            if freq[x] == c:
                ans = max(ans, x)
        return ans
```
</details>


## [2191. Sort the Jumbled Numbers](https://leetcode.com/problems/sort-the-jumbled-numbers/)

> 按给定的字典完成mapping
> 按照 1.mapping后的数值， 2.原数组中的位置 排序

<details>
    <summary> Python </summary>   
  
```python
def sortJumbled(self, mapping: List[int], A: List[int]) -> List[int]:
        nums = [list(map(int, list(str(x)))) for x in A]
        for num in nums:
            for i in range(len(num)):
                num[i] = mapping[num[i]]
        res = [int("".join(list(map(str, x)))) for x in nums]
        tmp = list(zip(res, list(range(len(A))), A))
        tmp.sort(key = lambda x: [x[0], x[1]])
        return [x[2] for x in tmp]

```
</details>

## [2192. All Ancestors of a Node in a Directed Acyclic Graph](https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/)

> BFS
> 从所有入度为0的结点开始，考察他们的子结点，子结点的parent是【子结点parent】与【当前父节点parent】的并集
> 当某个子结点的入度也为零，把它也加入后续队列中。

<details>
    <summary> Python </summary>   

```python
def getAncestors(self, n: int, A: List[List[int]]) -> List[List[int]]:
        parent, child = collections.defaultdict(set), collections.defaultdict(list)
        ans, indegree, dq = [], [0] * n, collections.deque()
        for a, b in A:
            parent[b].add(a)
            child[a].append(b)
            indegree[b] += 1
        for i in range(n):
            if indegree[i] == 0: dq.append(i)
        while dq:
            curr = dq.popleft()
            for nxt in child[curr]:
                parent[nxt] |= parent[curr]
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    dq.append(nxt)
        for i in range(n):
            ans.append(sorted(list(parent[i])))
        return ans
```
  
</details>

## [2193. Minimum Number of Moves to Make Palindrome](https://leetcode.com/problems/minimum-number-of-moves-to-make-palindrome/)

> 贪心法.

<details>
    <summary> C++ </summary>   
  
```cpp
public:
    int minMovesToMakePalindrome(string s) {
        int s_size = s.size();
        int result = 0;
        int start = 0, end = s_size - 1;
        while (end > start) {
            if (s[start] != s[end]) {
                int i = end; 
                while (i > start && s[i] != s[start]) { 
                    i -= 1; 
                }
                if (i == start) {
                    swap(s[start], s[start + 1]);
                    result += 1;
                }
                else {
                    while (i < end) {
                        swap(s[i], s[i + 1]);
                        result += 1;
                        i += 1;
                    }
                    start += 1; 
                    end -= 1;
                }
            }
            else {
                start += 1; 
                end -= 1;
            }
        }
        return result;
    }

```
</details>


<details>
    <summary> Python </summary>   
  
```python3
def minMovesToMakePalindrome(self, s: str) -> int:
        n, s = len(s), list(s)
        l, r, ans = 0, n - 1, 0
        while r > l:
            if s[l] != s[r]:
                kk = r
                while kk > l and s[kk] != s[l]:
                    kk -= 1
                if kk == l:
                    s[l], s[l + 1] = s[l + 1], s[l]
                    ans += 1
                else:
                    while kk < r:
                        s[kk], s[kk + 1] = s[kk + 1], s[kk]
                        ans += 1
                        kk += 1
                    l += 1
                    r -= 1
            else:
                l += 1
                r -= 1
        return ans

```
</details>



<details>
    <summary> Go </summary>   

```go
func minMovesToMakePalindrome(s string) int {
    n := len(s)
    tmp := []rune(s)
    l, r, ans := 0, n - 1, 0
    for r > l {
        if tmp[l] != tmp[r] {
            kk := r
            for kk > l && tmp[kk] != tmp[l] {
                kk -= 1
            }
            if kk == l {
                tmp[l], tmp[l + 1] = tmp[l + 1], tmp[l]
                ans += 1
            } else {
                for kk < r {
                    tmp[kk], tmp[kk + 1] = tmp[kk + 1], tmp[kk]
                    ans += 1
                    kk += 1
                }
                l += 1
                r -= 1
            }
        } else {
            l += 1
            r -= 1
        }
    }
    return ans
    return 1
}
```
  
</details>
