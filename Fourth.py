def sqrt(N):
    if N == 0:
        return 0

    left = 1
    right = N

    while left <= right:
        mid = (left + right) // 2
        square = mid * mid

        if square == N:
            return mid
        elif square < N:
            left = mid + 1
        else:
            right = mid - 1

    return left