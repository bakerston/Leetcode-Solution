## Comparator
#### CPP
```swift
sort(res.begin(), res.end(), [](const vector<int> &a, const vector<int> &b) {
            if (a[0] == b[0]) return a[1] < b[1];
            return a[0] < b[0];
        });
```

### JAVA
```swift
res.sort((a, b) -> {
            if (a[0] == b[0]) return a[1] - b[1];
            return a[0] - b[0];
        });
```
