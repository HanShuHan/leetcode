import sys


class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        if len(intervals) == 1:
            return 0

        intervals.sort(key=lambda x: x[1])
        prev_end = -sys.maxsize - 1
        count = 0
        for interval in intervals:
            if interval[0] >= prev_end:
                prev_end = interval[1]
                count += 1

        return len(intervals) - count
