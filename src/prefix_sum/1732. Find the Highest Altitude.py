class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        altitude = 0
        maxAlt = altitude

        for g in gain:
            altitude += g
            if altitude > maxAlt:
                maxAlt = altitude

        return maxAlt