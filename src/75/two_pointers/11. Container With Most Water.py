class Solution(object):
    def maxArea(self, height):
        size = len(height)
        left, right = 0, size - 1
        h = min(height[left], height[right])

        if size == 2:
            return h

        max_capacity = 0
        max_height = max(height)

        while left < right:
            w = right - left
            h = min(height[left], height[right])
            capacity = w * h

            if capacity > max_capacity:
                max_capacity = capacity

            if max_capacity == w * max_height:
                break

            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return max_capacity
