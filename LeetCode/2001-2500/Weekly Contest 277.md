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

> 数组排序，对于每一个数，看它是否跟左右邻居的差值都大于1，如果是，则为longly number。

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

> 两种方法：
> - 暴力求解
> - Bit-mask + DFS

