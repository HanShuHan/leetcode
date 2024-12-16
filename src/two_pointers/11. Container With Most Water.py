class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_h = max(height)
        max_area = 0

        while left < right:
            h1 = height[left]
            h2 = height[right]
            h = min(h1, h2)
            width = right - left
            area = width * h

            if area > max_area:
                max_area = area
            if h1 < h2:
                left += 1
            else:
                right -= 1

            if max_area >= max_h * width:
                break

        return max_area