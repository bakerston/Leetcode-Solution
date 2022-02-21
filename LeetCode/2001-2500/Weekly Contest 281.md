# Weekly Contest 281
 
 未参加
 
 ## [2180. Count Integers With Even Digit Sum](https://leetcode.com/problems/count-integers-with-even-digit-sum/)

> 求各位数字之和。

#### Go
```go
func sd(n int) int {  
    res := 0  
    ans := 0  
    for n != 0 {  
        res = n % 10  
        ans += res  
        n = n / 10  
    }  
    return ans
}  

func countEven(num int) int {
    var ans int = 0  
    for i := 1; i < num + 1; i++ {
        if (sd(i) % 2 == 0) {
            ans += 1
        }
    }
    return ans
}
```


## 2181. Merge Nodes in Between Zeros](https://leetcode.com/problems/merge-nodes-in-between-zeros/)

> 遇0跳过，否则累加每个节点之和。

#### Go
```go
func mergeNodes(h *ListNode) *ListNode {
        hh := new(ListNode)
	a := hh
	for h != nil {
		if h.Val != 0 {
			hh.Val += h.Val
			h = h.Next
		} else {
			if h.Next != nil {
				hh.Next = new(ListNode)
				hh = hh.Next
			}
			h = h.Next
		}
	}
	return a.Next
}
```



## [2182. Construct String With Repeat Limit](https://leetcode.com/problems/construct-string-with-repeat-limit/)

> 三种方法：优先队列、counter、双指针。
> 
#### PQ
#### Python
```swift
def repeatLimitedString(self, s: str, L: int) -> str:
        pq = [(-ord(k), v) for k, v in Counter(s).items()] 
        heapq.heapify(pq)
        hold, ans = [], ""
        
        while pq:
            k, num = heapq.heappop(pq)
            cur_ch = chr(-k)
            if not ans or ans[-1] != cur_ch:
                ans += cur_ch * min(L, num)
            if num > L:
                num -= L
                hold = [(-ord(cur_ch), num)]
            if hold:
                if not pq: return ans
                else:
                    k2, num2 = heapq.heappop(pq)
                    nxt_ch = chr(-k2)
                    ans += nxt_ch
                    num2 -= 1
                    if num2 > 0: heapq.heappush(pq, (-ord(nxt_ch), num2))
                    heapq.heappush(pq, hold.pop())                
        return ans
```

## [2183. Count Array Pairs Divisible by K](https://leetcode.com/problems/count-array-pairs-divisible-by-k/)

> Counter + 找最大公约数。

#### Python
```python3
def countPairs(self, nums: List[int], k: int) -> int:
        N, output = len(nums), 0
        divisors = []
        counter = Counter()
        
        for i in range(1, k + 1):
            if k % i == 0:
                divisors.append(i)

        for i in range(0, N):
            remainder = k // math.gcd(k, nums[i])
            output += counter[remainder]
            for divisor in divisors:
                if nums[i] % divisor == 0:
                    counter[divisor] += 1
            
        return output
```

