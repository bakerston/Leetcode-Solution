# Weekly Contest 276
#### 玩overcook去了，没参加

## [2138. Divide a String Into Groups of Size k](https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/)

> 遍历数组，每K个字符截成一个词，最后一个词长度不够的话，用X补齐。

#### CPP
```swift
public:
    vector<string> divideString(string s, int k, char fill) {
        vector<string> ans;
        string curr = "";
        for (int i = 0; i < s.size(); ++i) {
            if (i % k == 0 && i != 0) {
                ans.push_back(curr);
                curr = s[i];
            } else {
                curr.push_back(s[i]);
            }
        }
        if (curr.size() > 0) {
            int curLen = curr.size();
            while (curLen < k) {
                curr.push_back(fill);
                curLen += 1;
            }
            ans.push_back(curr);
        }
        
        return ans;        
    }
```

## [2139. Minimum Moves to Reach Target Score](https://leetcode.com/problems/minimum-moves-to-reach-target-score/)

> 贪心法：每个【加倍】的操作，一定要用在最大可能的数上。比如从1到9，【4加倍成8】等同于4步，而【3加倍成6】只等同于3步。
> 因此，从target倒推（【加倍】变为【减半】，【加一】变成【减一】），只要能用【减半】就用，这里，**能用**的前提只有两个
> - 还有剩余的加倍操作。
> - 当前数字是偶数。
> 直到用完了【加倍】操作，或者达到数字**1**。

#### CPP
```swift
public:
    int minMoves(int target, int maxDoubles) {
        int ans = 0;
        while (target > 1 && maxDoubles > 0) {
            if (target % 2 == 1) {
                target -= 1;
            } else {
                target /= 2;
                maxDoubles -= 1;
            }            
            ans += 1;
        }        
        return ans + (target - 1);
        
    }
```

## [2140. Solving Questions With Brainpower](https://leetcode.com/problems/solving-questions-with-brainpower/)
> DP, 从后往前（倒叙）DP。原因在于从前往后的话，不构成1对1的DP条件。
> 基础步骤是：倒叙遍历时，对于每一个问题[points, power]，我们有两种选择，【做】还是【不做】：
> - 如果【做】，我们的分数是多少呢，我们首先有这个问题的分数，也就是【points】，第二部分就是【从当天往后第power+1天的分数】，因为我们选择了【做】，那么之后的【power】天内都是不需要考虑的，直接跳到【power+1】天。
> - 如果【不做】，我们的分数就跟之后一天的一样。
> 直至第0天，由于分数是按照日期递增的，直接返回第0天能得到的最大分数即可

#### Python
```swift
def mostPoints(self, A: List[List[int]]) -> int:        
        n = len(A)
        if n == 1: return A[0][0]
        
        dp = [0] * (n - 1) + [A[-1][0]] 

        for i in range(n - 2, -1, -1):            
            p, t = A[i]
            if i + t < n - 1:
                p += dp[i + t + 1]
            dp[i] = max(p, dp[i + 1])
            
        return dp[0]
```

## [2141. Maximum Running Time of N Computers](https://leetcode.com/problems/maximum-running-time-of-n-computers/)
> 把电池按照电量排序，只看【电量最大的后n节电池】，把前面的小电池等效为一块电池【outer】。
> 在这N块电池里，从小到大遍历（【0】【1】【2】... 【n-1】：
> - 假设我们把【outer】的全部电量都给【0】号电池：
>   - 如果【0】的电量仍然不够【1】号电池的电量，说明系统最大的运行时间就是【0】+【outer】
>   - 否则，我们把【outer】的电量匀出一部分给【0】，使其等于【1】号电量；
> - 接下来，我们看【outer】剩下的电量，均分给【0】和【1】，看他俩的电量够不够【2】号电池的电量。
>   - 如果【0】【1】的电量不够【2】号电量，说明系统最大运行时间是 （【1】+【2】+【outer】）/2,
>   - 否则，我们把【outer】的电量均出一部分给【0】和【1】，使其等于【2】号电量。
>   - ....直到分完电量，或者走到最后一块电池【n-1】

#### Python
```swift
def maxRunTime(self, n: int, A: List[int]) -> int:
        A.sort()
        outer, ans, presum = sum(A[:-n]), 0, 0
        A = A[-n:]

        for i, x in enumerate(A[:-1]): 
            presum += x 
            if A[i + 1] * (i + 1) - presum > outer: 
                return (presum + outer) // (i + 1)
        return (presum + A[-1] + outer) // n
```
