def search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid

        if arr[low] <= arr[mid]:
            if arr[low] <= key < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if arr[mid] < key <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1


arr = [5,6,7,8,9,10,1,2,3]
print(search(arr, 10))