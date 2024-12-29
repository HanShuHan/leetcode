class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1,
        max_height = max(height)
        max_volume = 0

        while left < right:
            width = right - left
            volume = width * min(height[left], height[right])

            if volume > max_volume:
                max_volume = volume

            if volume == width * max_height:
                break

            if height[left] >= height[right]:
                right -= 1
            else:
                left += 1

        return max_volume
