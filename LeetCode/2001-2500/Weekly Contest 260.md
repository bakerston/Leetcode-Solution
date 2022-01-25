# Weekly Contest 260

完成4题，用时1:04:54\
2次错误，总成绩1:14:54\
[排名 **90/11274**](https://leetcode.com/contest/weekly-contest-260/ranking/4/)。

## [2016. Maximum Difference Between Increasing Elements](https://leetcode.com/problems/maximum-difference-between-increasing-elements/)

>买卖股票
>遍历数组，记录历史遇到的最小数，用当天的数减去历史最小数，就是当天卖出的利润\
>对于每一天的利润，找出最大值\
>O(N)
>


#### C++
```swift
public:
    int maximumDifference(vector<int>& A) {
        int ans = 0, mi = A[0];
        for (int a : A){
            ans = max(ans, a - mi);
            mi = min(mi, a);
        }
        return ans > 0 ? ans : -1;
    }
```

#### Java
```swift
public int maximumDifference(int[] A) {
        int ans = 0, mi = A[0];
        for (int a : A){
            ans = Math.max(ans, a - mi);
            mi = Math.min(mi, a);
        }
        return ans > 0 ? ans : -1;
    }
```

#### Python
```swift
def maximumDifference(self, nums: List[int]) -> int:
        res = 0
        mi, ma = math.inf, -math.inf
        for a in nums:
            res = max(res, a - mi)
            mi = min(mi, a)
            ma = max(ma, a)
        return res if res > 0 else -1
```

## [2017. Grid Game](https://leetcode.com/problems/grid-game/)

> Prefix法。
> 第二个机器人只有二选一：
> - A[0][K:]
> - A[1][:K]
> K是第一个机器人的转向下的列数。
> 对于每一个可能的K，计算第二个机器人能取得的最大值，选出最大值最小的K。

#### C++
```swift
public:
    long long gridGame(vector<vector<int>>& A) {
        long long n = A[0].size(), a = 0, b = 0, ans = LLONG_MAX;
        vector<long long> pre_a(1, 0), pre_b(1, 0);
        for (int i = 0; i < n; ++i){
            a += A[0][i];
            b += A[1][i];
            pre_a.push_back(a);
            pre_b.push_back(b);
        }       
        for (int i = 0; i < n; ++i){
            long long cur = max(pre_b[i], pre_a[n] - pre_a[i + 1]);
            ans = min(ans, cur);
        }
        return ans;
    }
```
#### Java
```swift
public long gridGame(int[][] A) {
        long topSum = Arrays.stream(A[0]).asLongStream().sum(), bottomSum = 0;
        long ans = Long.MAX_VALUE;
        for (int i = 0; i < A[0].length; ++i) {
            topSum -= A[0][i];
            ans = Math.min(ans, Math.max(topSum, bottomSum));
            bottomSum += A[1][i];
        }
        return ans;
    }
```

#### Python
```swift
def gridGame(self, A: List[List[int]]) -> int:
        top, bot = sum(A[0]), 0
        ans = math.inf
        for i in range(len(A[0])):
            top -= A[0][i]
            ans = min(ans, max(top, bot))
            bot += A[1][i]
        return ans
```


## [2018. Check if Word Can Be Placed In Crossword](https://leetcode.com/problems/check-if-word-can-be-placed-in-crossword/)

> 设word长度为N
> 找出原2D数组中所有长度等于N的连续空格，看空格是否为空，或者已有的字母是否与word对应位置的字母相同。
> 

#### Python
```swift
def placeWordInCrossword(self, A: List[List[str]], word: str) -> bool:
        m, n = len(A), len(A[0])
        k = len(word)
        if n >= k:
            for row in A:
                cur = ("".join(row)).split("#")
                for w in cur:
                    if len(w) == k:
                        find = True
                        for i in range(k):
                            if w[i] not in [" ", word[i]]:
                                find = False
                                break
                        if find == True: return True
                        find = True
                        for i in range(k):
                            if w[i] not in [" ", word[k - i - 1]]:
                                find = False
                                break
                        if find == True: return True

        if m >= k:
            A = list(zip(*A[::-1]))
            for row in A:
                cur = ("".join(row)).split("#")
                for w in cur:
                    if len(w) == k:
                        find = True
                        for i in range(k):
                            if w[i] not in [" ", word[i]]:
                                find = False
                                break
                        if find == True: return True
                        find = True
                        for i in range(k):
                            if w[i] not in [" ", word[k - i - 1]]:
                                find = False
                                break
                        if find == True: return True
        return False
```

## [2019. The Score of Students Solving Math Expression](https://leetcode.com/problems/the-score-of-students-solving-math-expression/)

> [我的LeetCode题解](https://leetcode.com/problems/the-score-of-students-solving-math-expression/discuss/1486306/PythonJava-Explanation-with-pictures-DP)
> DP。

#### Java
```swift
import java.util.Hashtable;
class Solution {
    public int calculate(String s) {
        int i = 0;
        Stack<Integer> stack = new Stack<>();
        char operator = '+';
        int num = 0;
        while (i < s.length()) {
            char ch = s.charAt(i++);
            if (ch >= '0' && ch <= '9') num = ch - '0';
            if (i >= s.length() || ch == '+' || ch == '*') {
                if (operator == '+') stack.push(num);
                else if (operator == '*') stack.push(stack.pop() * num);
                operator = ch;
                num = 0;
            }
        }
        return stack.stream().mapToInt(Integer::intValue).sum();
    }
    
    public int scoreOfStudents(String s, int[] A) {
        int n = (int)(s.length() / 2 + 1);
        Set<Integer>[][] res = new Set[n][n];
        for (int i = 0; i < n; ++i){
            res[i][i] = new HashSet<>();
            res[i][i].add(s.charAt(2 * i) - '0');
        }
        for (int dif = 1; dif < n; ++dif){
            for (int start = 0; start < n - dif; ++start){
                int end = start + dif;
                res[start][end] = new HashSet<>();
                for (int i = start * 2 + 1; i < end * 2; i += 2){
                    if (s.charAt(i) - '+' == 0){
                        for (int a : res[start][(int)(i / 2)]){
                            for (int b : res[(int)(i / 2 + 1)][end]){
                                if (a + b <= 1000) res[start][end].add(a + b);
                            }
                        }
                    } else {
                        for (int a : res[start][(int)(i / 2)]){
                            for (int b : res[(int)(i / 2 + 1)][end]){
                                if (a * b <= 1000) res[start][end].add(a * b);
                            }
                        }
                    }
                }              
            }
        }
        
        int correct = calculate(s), ans = 0;
        for (int a : A){
            if (a == correct) ans += 5;
            else if (res[0][n - 1].contains(a)) ans += 2;
        }
        return ans;
        
    }
}
```


#### Python
```swift
def scoreOfStudents(self, s: str, A: List[int]) -> int:
        c = collections.Counter(A)
        n = len(s) // 2 + 1
        res = [[set() for _ in range(n)] for j in range(n)]
        for i in range(n):
            res[i][i].add(int(s[2 * i]))
        for dif in range(1, n):
            for start in range(n - dif):
                end = start + dif
                curset = set()
                for i in range(start * 2 + 1, end * 2, 2):
                    if s[i] == "+":
                        for a in res[start][i // 2]:
                            for b in res[i//2 + 1][end]:
                                if a + b <= 1000:
                                    curset.add(a + b)
                    else:
                        for a in res[start][i // 2]:
                            for b in res[i//2 + 1][end]:
                                if a * b <= 1000:
                                    curset.add(a * b)
                res[start][end] = curset
        ans = 0
        crt = eval(s)
        for i in res[0][-1]:
            if i in c:
                if i == crt:
                    ans += 5 * c[i]
                else:
                    ans += 2 * c[i]
        return ans
```



