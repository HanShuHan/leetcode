class Solution(object):
    def findMinArrowShots(self, points):
        points_len = len(points)

        if points_len == 1:
            return 1

        points.sort(key=lambda x: x[1])
        prev_end = points[0][1]
        count = 1

        for i in range(1, points_len):
            if points[i][0] > prev_end:
                prev_end = points[i][1]
                count += 1

        return count
