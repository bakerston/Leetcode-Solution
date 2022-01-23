# Weekly Contest 274  

完成4题，用时1:08:23\
0次错误，总成绩1:08:23\
[排名 **76/14086**](https://leetcode.com/contest/weekly-contest-274/ranking/4/)

## [2124. Check if All A's Appears Before All B's](https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/)

> 检查字符串中有没有'ba'

#### **Python**
```swift
def checkString(self, s: str) -> bool:
        find = False
        for ch in s:
            if ch == 'b':
                find = True
            else:
                if find:
                    return False
        return True
```

## [2125. Number of Laser Beams in a Bank](https://leetcode.com/problems/number-of-laser-beams-in-a-bank/)

> 计算相邻两层中laser数量的乘积，连乘。

#### Python
```swift
def numberOfBeams(self, A: List[str]) -> int:
        ans = []
        for row in A:
            c = collections.Counter(row)
            if c['1'] > 0:
                ans.append(c['1'])
        if len(ans) < 2: return 0
        res = 0
        for i in range(len(ans) - 1):
            res += ans[i] * ans[i + 1]
        return res
```

## [2126. Destroying Asteroids](https://leetcode.com/problems/destroying-asteroids/)

> 数组排序，依次对比mass质量与排序后的数组元素大小。
#### Python
```swift
def asteroidsDestroyed(self, mass: int, A: List[int]) -> bool:
        A.sort()
        for a in A:
            if mass < a:
                return False
            mass += a
        return True
```

## [2127. Maximum Employees to Be Invited to a Meeting](https://leetcode.com/problems/maximum-employees-to-be-invited-to-a-meeting/)

> [LeetCode题解](https://leetcode.com/problems/maximum-employees-to-be-invited-to-a-meeting/discuss/1661178/Explanation-with-pictures.)\


#### Python

```swift
def maximumInvitations(self, A: List[int]) -> int:
		# First, we find the largest circle.
        n, maxc = len(A), 0
        seen = [0] * n
        for idx in range(n):
		
			# If a people hasn't been visited:
            if seen[idx] == 0:
                
				# start is for locating the first visited people, cur_people stands 
				#for the current people we are visiting, we use curset to store all 
				# the visited people in this iteration.
				start = idx
                cur_people = idx
                curset = set()
				
				# As long as we are visiting new people, we keep finding his/her favorite.
                while seen[cur_people] == 0:
                    seen[cur_people] = 1
                    curset.add(cur_people)
                    cur_people = A[cur_people]
					
				# Until we find the first visited people. Depends on if this 
				# visited people has been visited in eariler iteration or just this iteration.
				if cur_people in curset:       # if current people is in current set, meaning we have found a new circle
                    cursum = len(curset)
					
					# use 'start' to find the distance from the first visited people in this iteration 
					# to this current people.
                    while start != cur_people:
                        cursum -= 1
                        start = A[start]
                    maxc = max(maxc, cursum)
                                       
		# Then we try to find the sum of largest arms. Firstly, find all mutal-favorite peoples.
        pair = []
        visited = [0] * n
        for i in range(n):
		
			# If a is b's favorite and vise versa, we put them in 'pair'.
            if A[A[i]] == i and visited[i] == 0:
                pair.append([i, A[i]])
                visited[i] = 1
                visited[A[i]] = 1
		
		# for every people I, find out all the people whos favorite is I.
        res = 0
        child = collections.defaultdict(list)
        for i in range(n):
            child[A[i]].append(i)
        
        for a, b in pair:
            # max arm length start from first people a
            maxa = 0
            dq = collections.deque()
            for cand in child[a]:
                if cand != b:
                    dq.append([cand, 1])
            while dq:
                cur, n = dq.popleft()
                maxa = max(maxa, n)
                for nxt in child[cur]:
                    dq.append([nxt, n + 1])
                    
            # max arm length start from first people b
            maxb = 0
            dq = collections.deque()
            for cand in child[b]:
                if cand != a:
                    dq.append([cand, 1])
            while dq:
                cur, n = dq.popleft()
                maxb = max(maxb, n)
                for nxt in child[cur]:
                    dq.append([nxt, n + 1])
            
			# Thus the total length is the two longest arm plus 2 (a and b themselves)
            res += 2 + maxa + maxb
			
		# select the larger one as the answer.
        return max(maxc, res)  
```
