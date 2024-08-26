def selection_sort(arr: list[int]) -> list[int]:
    # array size
    size = len(arr)

    # no sorting needed if the array size is less than two
    if size <= 1:
        return arr

    # sorts the min starting from the left
    for i in range(size - 1):
        # min as each section's start element
        min_idx = i
        # records the current min's index
        for j in range(i + 1, size):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # swaps the two elements if the initial min is not the min
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

    # returns the sorted array
    return arr
