def search(arr, target):
    left = 0
    right = len(arr) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            result = mid
            left = mid + 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result

arr = [1, 2, 4, 6, 7, 7, 7, 8, 10]
target = 7

index = search(arr, target)
print(index)