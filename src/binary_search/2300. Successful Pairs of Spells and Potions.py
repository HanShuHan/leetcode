import bisect


class Solution(object):
    def successfulPairs(self, spells, potions, success):
        potions_size = len(potions)
        potions.sort()
        result = []

        for spell in spells:
            min_potion = (success + spell - 1) // spell

            index = bisect.bisect_left(potions, min_potion)
            result.append(potions_size - index)

        return result
