import sys


class Solution(object):
    def findMinArrowShots(self, points):
        if len(points) == 1:
            return 1

        count = 0
        prev_end = -sys.maxsize - 1
        points.sort(key=lambda x: x[1])
        for point in points:
            if point[0] > prev_end:
                count += 1
                prev_end = point[1]

        return count
