# Weekly Contest 277  

举铁，没参加。幸好没参加，最后一题照我后来做出来的速度，估计名次1000+了。

## [2148. Count Elements With Strictly Smaller and Greater Elements](https://leetcode.com/problems/count-elements-with-strictly-smaller-and-greater-elements/)

>双指针法\
>先把数组排序，找出第一个大于A[0]和第一个小于A[-1]的值的下标i,j\
>比如[0,0,1,2,3,6,6],第一个大于A[0]的下标是2，第一个小于A[-1]的下标是4.\
>一共有j - i + 1个数。
>

#### C++
```swift
int countElements(vector<int>& A) {
        sort(A.begin(), A.end());
        int n = A.size();
        
        if (n < 3) return 0;
        
        int i = 1, j = n - 2;
        while (i < n && A[i] == A[0])
            ++i;
        while (j >= 0 && A[j] == A[n - 1])
            --j;
        return max(0, j - i + 1);       
    }
```

## [2149. Rearrange Array Elements by Sign](https://leetcode.com/problems/rearrange-array-elements-by-sign/)

> 分割正数和负数，按顺序填充ans.

#### C++
```swift
vector<int> rearrangeArray(vector<int>& nums) {
        vector<int> pos, neg;
        for (int num : nums) {
            if (num > 0)
                pos.push_back(num);
            else
                neg.push_back(num);
        }
        vector<int> ans;
        for (int i = 0; i < pos.size(); ++i) {
            ans.push_back(pos[i]);
            ans.push_back(neg[i]);
        }
        return ans;
    }
```

## [2150. Find All Lonely Numbers in the Array](https://leetcode.com/problems/find-all-lonely-numbers-in-the-array/)

> 数组排序，对于每一个数，看它是否跟左右邻居的差值都大于1，如果是，则为lonely number。

#### C++
```swift
vector<int> findLonely(vector<int>& A) {
        sort(A.begin(), A.end());
        vector<int> ans;
        int n = A.size();
        
        for (int i = 0; i < n; ++i) {
            bool alone = true;
            if (i > 0)
                alone &= A[i] - A[i - 1] > 1;
            if (i < n - 1)
                alone &= A[i + 1] - A[i] > 1;
            if (alone)
                ans.push_back(A[i]);
        }
        
        return ans;
    }
```

## [2151. Maximum Good People Based on Statements](https://leetcode.com/problems/maximum-good-people-based-on-statements/)

### 两种方法：


### Bitmask + 暴力求解
> 注意到最多15个人，每个人可能是好人（1）或者坏人（0），用二进制来表示每个人的状态，需要考虑2^15 ~ 30000种可能。\
> 对于每种可能，我们需要检查每一个好人对于其他人的所有评价\
> **（不需要考虑坏人的评价，因为我们无法判断坏人评价是对还是错**\
> 比如说：
> 某个二进制数“1000100...”，第一个人是好人（1），我们需要看他对于剩下所有人的评价\
> - 如果一个其他人是好人（比如这个二进制数的第五位），但是A[0][4]是0----表示第一个人说第五个人是坏人，与事实相悖，说明这个二进制数不是正确的。
> - 如果一个其他人是坏人（比如这个二进制数的第二位），但是A[0][1]是1----表示第一个人说第二个人是好人，同样与事实相悖，说明这个二进制数不是正确的。
> 
> 如果两种情况都没发生，说明至少对于第一个人，这个二进制数是正确的。  
> 我们遍历这个二进制中所有好人位，如果每一个好人都能通过上述的检查，说明这个二进制是正确的。记录当前这个二进制数中有多少位1，也就是好人的数量。  
> 穷举所有的N位二进制数（长度不够N的，前面加0补齐），找出1位最多的【正确的】二进制数。  

#### Python
```swift
def maximumGood(self, A: List[List[int]]) -> int:
        n = len(A)
        def helper(num):
            res = bin(num)[2:]
            return "0" * (n - len(res)) + res
        ans = 0
        for num in range(2**n):
            curr = helper(num)
            wrong = False
            for i, x in enumerate(curr):
                if wrong:
                    continue
                if x == "1":
                    for j in range(n):
                        if (curr[j] == "0" and A[i][j] == 1)\
                        or (curr[j] == "1" and A[i][j] == 0):
                            wrong = True
                            continue
                if wrong: continue
            if not wrong:
                ans = max(ans, collections.Counter(curr)["1"])
        return ans
```



### Bit-mask + DFS

