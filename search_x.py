n = int(input())
a = [int(x) for x in input().split()]
k = int(input())

low = 0
high = len(a) - 1
res = -1

while low <= high:
    mid = (low+high) // 2  
    if a[mid] == k:
        res = mid
        break
    elif a[mid] < k:
        low = mid + 1
    elif a[mid] > k:
        high = mid - 1
print(res)

