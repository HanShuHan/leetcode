from collections import Counter


class Solution(object):
    # def uniqueOccurrences(self, arr):
    #     arr_len = len(arr)
    #
    #     if arr_len == 1:
    #         return True
    #
    #     d = defaultdict(int)
    #
    #     for num in arr:
    #         d[num] += 1
    #
    #     vals = d.values()
    #
    #     return len(vals) == len(set(vals))

    def uniqueOccurrences(self, arr):
        arr_len = len(arr)

        if arr_len == 1:
            return True

        count = Counter(arr)

        vals = count.values()

        return len(vals) == len(set(vals))
