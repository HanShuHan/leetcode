class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        intervals_len = len(intervals)

        if intervals_len == 1:
            return 0

        intervals.sort(key=lambda x: x[1])
        prev_end = intervals[0][1]
        count = 0

        for i in range(1, intervals_len):
            if intervals[i][0] < prev_end:
                count += 1
            else:
                prev_end = intervals[i][1]

        return count
