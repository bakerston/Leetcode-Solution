# Biweekly Contest 70  

完成4题，用时24：36\
两次错误，总成绩34：36\
[排名 **58/17655**](https://leetcode.com/contest/biweekly-contest-70/ranking/3/)。

## [2144. Minimum Cost of Buying Candies With Discount](https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/)

> 贪心法，商品按照价格倒序排序（从高到低），每购买两个商品，可以免费获得第三个。
> 
> [付费][付费][免费] [付费][付费][免费] ...
> 
> 最后，加上剩下的凑不够3个的商品。比如5个商品，最后会剩下两个价格最低的，全部是付费的。

#### **Python**
```swift
def minimumCost(self, A: List[int]) -> int:
        A.sort(reverse = True)
        n, ans = len(A), 0
        for i in range(n // 3):
            ans += A[3 * i] + A[3 * i + 1]
        res = n % 3

        return ans if n % 3 == 0 else ans + sum(A[-(n % 3):])
```

## [2145. Count the Hidden Sequences](https://leetcode.com/problems/count-the-hidden-sequences/)
