import bisect


class Solution(object):
    def successfulPairs(self, spells, potions, success):
        # spells = [5,1,3]
        # potions = [1,2,31,4,15]

        potions.sort()
        spells_len = len(spells)
        potions_len = len(potions)
        result = []

        for i in range(spells_len):
            min_potion = (success + spells[i] - 1) // spells[i]
            index = bisect.bisect_left(potions, min_potion)

            result.append(potions_len - index)

        return result
