class Solution(object):
    # def largestAltitude(self, gain):
    #     gain_len = len(gain)
    #
    #     altitudes = [0] * (gain_len + 1)
    #     total = 0
    #
    #     for i in range(gain_len):
    #         total += gain[i]
    #         altitudes[i + 1] = total
    #
    #     return max(altitudes)

    def largestAltitude(self, gain):
        total = highest = 0

        for g in range(gain):
            total += g
            if total > highest:
                highest = total

        return highest
