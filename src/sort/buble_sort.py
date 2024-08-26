def buble_sort(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr
    # algorithm
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    # return the answer
    return arr
