import sys
line1 = sys.stdin.readline().strip()
line2 = sys.stdin.readline().strip()

nums = list(map(int, line2.split()))
n = len(nums)
change = False
for idx in range(n - 1):
    if not change:
        if len(str(nums[idx])) == len(str(nums[idx + 1])):
            l, r =list(str(nums[idx])), list(str(nums[idx + 1]))
            m = len(l)
            for j in range(m):
                if (m > 1 and (int(l[j]) > 1 or (j > 0 and int(l[j]) > 0))) or m == 1 and int(l[j]) > 0:
                    r[j] = str(int(l[j]) - 1)
                    nums[idx + 1] = int(''.join(r))
                    change = True
                    break
                elif int(r[j]) < 9:
                    l[j] = str(int(r[j]) + 1)
                    nums[idx] = int(''.join(l))
                    change = True
                    break 
    else:
        break
if not change:
    print("impossible")
else:
    for i in range(n):
        print(nums[i], end = " ")
        
            
