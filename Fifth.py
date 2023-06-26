def search(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        mid = (left + right) // 2

        if arr[mid] == mid:
            left = mid + 1
        else:
            right = mid

    return left