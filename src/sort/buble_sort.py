def buble_sort(arr: list[int]) -> list[int]:
    # array size
    size = len(arr)

    # no sorting needed if the array size is less than two
    if size <= 1:
        return arr

    # algorithm
    for i in range(size - 1):
        for j in range(size - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    # return the answer
    return arr
