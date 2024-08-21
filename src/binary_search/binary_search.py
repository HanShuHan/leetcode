def binary_search(target: int, arr: list[int]) -> int:
    # no numbers
    if len(arr) == 0:
        return -1
    # guessing
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    # not found
    return -1
