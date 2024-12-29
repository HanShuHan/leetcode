def insertion_sort(arr: list[int]) -> list[int]:
    # array size
    size = len(arr)

    # no sorting needed if the array size is less than two
    if size <= 1:
        return arr

    # starts sorting from the 2nd element of the right unsorted group
    for i in range(1, size):
        key = arr[i]  # the element being sorted
        j = i - 1  # the last element's index of the left sorted group
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]  # copy the left element's value to the right element
            j -= 1
        # inserts the sorted element into the left sorted group
        if arr[i] != key:
            arr[j + 1] = key

    # returns the sorted array
    return arr


if __name__ == '__main__':
    print(insertion_sort([5, 4, 3, 2, 1]))
