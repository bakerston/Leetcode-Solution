## Weekly Contest 276
#### 玩overcook去了，没参加

### 2138. Divide a String Into Groups of Size k
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

### 2139. Minimum Moves to Reach Target Score
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
