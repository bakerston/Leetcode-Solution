# Weekly Contest 272  

完成4题，用时0:23:40\
0次错误，总成绩0:23:40\
[排名 **128/15428**](https://leetcode.com/contest/weekly-contest-272/ranking/6/)\
太他妈卷了

## [2108. Find First Palindromic String in the Array](https://leetcode.com/problems/find-first-palindromic-string-in-the-array/)

> 遍历数组，返回第一个回文词\
> 如果遍历完还没找到，就返回""

#### **C++**
```swift
string firstPalindrome(vector<string>& words) {
    for (string word : words)
        if (word == string(rbegin(word), rend(word)))
            return word;
    return "";
}
```
#### Java
```swift
public String firstPalindrome(String[] words) {
        for (String word : words) {
            boolean find = true;
            for (int i = 0; i < word.length() / 2; ++i) {
                if (word.charAt(i) != word.charAt(word.length() - 1 - i)) {
                    find = false;
                    continue;
                }
            }
            if (find) {
                return word;
            }            
        }        
        return "";
    }
```

#### **Python**
```swift
def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if word == word[::-1]:
                return word
        return ""
```

## [2109. Adding Spaces to a String](https://leetcode.com/problems/adding-spaces-to-a-string/)

> 双指针法，【i】，【j】分别是【原字符串s】和【空白位置数组space】的下标。\
> 构建一个新的字符串，从""开始\
> 递增i，每当i=space[j]的时候，说明到了一个新的空格位置，插入一个空格，j加一。\
> 之后再附加上【s】的第i个字符，i加一。\
> 直到i到达各自尾端。

#### Python
```swift
def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = ""
        n, m = len(s), len(spaces)
        i, j = 0, 0
        
        while i < n:
            if j < m and spaces[j] == i:
                ans += " "
                j += 1
            else:
                ans += s[i]
                i += 1
        return ans
```

## [2110. Number of Smooth Descent Periods of a Stock](https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock)

> [LeetCode题解](https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/discuss/1635104/CPPJAVAPython-Explanation-with-pictures.)

#### C++
```swift
public:
    long long getDescentPeriods(vector<int>& A) {
        int n = A.size();
        long long ans = 0, cur = 1;
        
        for (int i = 1; i < n; ++i) {
            if (A[i] == A[i - 1] - 1)
                cur += 1;
            else {
                ans += cur * (cur + 1) / 2;
                cur = 1;
            }
        }
        
        return ans + cur * (cur + 1) / 2;
    }
```

#### Java
```swift
public long getDescentPeriods(int[] A) {
        int n = A.length;
        long ans = 0, cur = 1;
        
        for (int i = 1; i < n; ++i) {
            if (A[i] == A[i - 1] - 1)
                cur += 1;
            else {
                ans += cur * (cur + 1) / 2;
                cur = 1;
            }
        }
        
        return ans + cur * (cur + 1) / 2;
    }
```

#### Python
```swift
def getDescentPeriods(self, A: List[int]) -> int:
        n = len(A)
        ans, cur = 0, 1

        for i in range(1, n):
            if A[i] == A[i - 1] - 1:
                cur += 1
            else:
                ans += cur * (cur + 1) // 2
                cur = 1
        return ans + cur * (cur + 1) // 2
```

## [2111. Minimum Operations to Make the Array K-Increasing](https://leetcode.com/problems/minimum-operations-to-make-the-array-k-increasing/)

> [LeetCode题解](https://leetcode.com/problems/minimum-operations-to-make-the-array-k-increasing/discuss/1635026/Python-Explanation-with-pictures-LIS)\
> 基本思路是寻找K个子字符串的【最长递增子序列】(longest increasing subsequence)\
> 题目要求的是每隔K个字符之间要递增\
> 比如K=2,那么1，3，5，7要递增，0，2，4，6 要递增，而2，3之间的大小关系并不重要\
> 因此，我们按照间距K，把原字符串分割成K个子字符串\
> 比如K=3，那么第一个串是0，3，6，9，第二个串是1，4，7，10，第三个串是2，5，8，...\
> 对于每一个子串，我们要用最小的操作，使其全部递增（严格来说是【不下降】，不过不影响整体思路）\
> 那么我们要找出原来的子串中，有多少数已经满足【递增】的条件，我们只需要改变剩下的数的大小即可\
> 比如子串有10个数，我们能找到长度为6的递增子序列，说明我们只需要改变剩下10-6=4个数的大小\
> LIS的问题就比较简单了，时间复杂度O(N logN)


#### Python

```swift
def kIncreasing(self, A: List[int], k: int) -> int:
        def LIS(arr):
            ans = []
            for a in arr:
                idx = bisect.bisect_right(ans, a)
                if idx == len(ans):
                    ans.append(a)
                else:
                    ans[idx] = a       
            return len(ans)
        
        ans, n = 0, len(A)
        
        for start in range(k):
            cur, idx = [], start
            while idx < n:
                cur.append(A[idx])
                idx += k
            ans += len(cur) - LIS(cur)
        return ans
```
