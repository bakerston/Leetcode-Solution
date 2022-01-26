# Biweekly Contest 61

完成4题，用时28:54\
0次错误，总成绩28:54\
[排名 **91/9137**](https://leetcode.com/contest/biweekly-contest-61/ranking/3/)。

## [2006. Count Number of Pairs With Absolute Difference K](https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/)

> HashTable
> 对于nums里每个数num，找num+k是否存在。
>


#### Python
```swift
def countKDifference(self, nums: List[int], k: int) -> int:
        c = collections.Counter(nums)
        ans = 0
        for i in c:
            if i + k in c:
                ans += c[i] * c[i + k]
        return ans
```

## [2007. Find Original Array From Doubled Array](https://leetcode.com/problems/find-original-array-from-doubled-array/)

> 依然是Hashtable
> 从小到大访问数组A，对于每个数字a，如果存在尚未被访问的2a，则同时去掉【a】和【2a】，把【a】添加到待返回的原数组中。  
> 如果遇到了某个数【x】，发现并不存在【2x】，返回[]。  
> 否则，返回原数组。
> 
#### Python
```swift
def findOriginalArray(self, A: List[int]) -> List[int]:
        c = collections.Counter(A)
        keys = sorted(list(c.keys()))
        n, idx, ans = len(keys), 0, []
        
        while idx < n:
            cur = keys[idx]
            if cur == 0:
                if c[cur] % 2: return []
                else: ans.extend([0] * (c[cur] // 2))
            elif c[cur] > 0:
                if c[2 * cur] < c[cur]: return []
                else:
                    ans.extend(c[cur] * [cur])
                    c[2 * cur] -= c[cur]
                    c[cur] = 0
            idx += 1
        return ans
```


## [2008. Maximum Earnings From Taxi](https://leetcode.com/problems/maximum-earnings-from-taxi/)

> Binary Search + DP
> 把所有ride按照结束地点【end】由小到大排序。
> O（N logN）
> 

#### Python
```swift
def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        ans = []
        A.sort(key = lambda x: x[1])
        for start, end, tip in A:
            cur = end - start + tip
            idx = bisect.bisect_right(ans, [start, math.inf])
            if idx > 0:
                cur += ans[idx - 1][1]
            if not ans or cur > ans[-1][1]:
                ans.append([end, cur])
        return ans[-1][1]
```

## [2009. Minimum Number of Operations to Make Array Continuous](https://leetcode.com/problems/minimum-number-of-operations-to-make-array-continuous/)

> [我的LeetCode题解](https://leetcode.com/problems/the-score-of-students-solving-math-expression/discuss/1486306/PythonJava-Explanation-with-pictures-DP)\
> Binary Search
> 
#### C++
```swift
public:
    int minOperations(vector<int>& A) {
        int n = A.size();
        sort(A.begin(), A.end());
        int ans = n - 1, cur = 1;
        vector<int> uniq(1, 1);
        for (int i = 1; i < n; ++i){
            if (A[i] != A[i - 1]) cur += 1;
            uniq.push_back(cur);
        }
        vector<int>::iterator upper;
        for (int i = 0; i < n; ++i){
            int a = A[i];
            upper = upper_bound(A.begin(), A.end(), a + n - 1);
            int idx = upper - A.begin();
            int cur_uniq = max(0, uniq[idx - 1] - uniq[i]) + 1;
            ans = min(ans, n - cur_uniq);
        }
        return ans;       
    }
```

#### Java
```swift
public int minOperations(int[] A) {
        Arrays.sort(A);
        int n = A.length, maxn = 0;
        Deque<Integer> window = new ArrayDeque<>();
        for (int num : A){
            while (window.size() > 0 && num - window.peekFirst() >= n)
                window.poll();
            if (window.size() == 0 || !window.peekLast().equals(num))
                window.offer(num);
            maxn = Math.max(maxn, window.size());
        }
        return n - maxn;    
    }
```


#### Python
```swift
def minOperations(self, nums: List[int]) -> int:
        A.sort()
        n = len(A)
        ans = n - 1
        uniq, cur = [1], 1
        
        for i in range(1, n):
            if A[i] != A[i - 1]: 
                cur += 1
            uniq.append(cur)
        
        for i in range(n):
            a = A[i]
            idx = bisect.bisect_right(A, a + n - 1)
            cur_uniq = max(0, uniq[idx - 1] - uniq[i]) + 1
            ans = min(ans, n - cur_uniq)

        return ans
```
