class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        flowerbed.insert(0, 0)
        flowerbed.append(0)
        i = 1

        while n > 0 and i < len(flowerbed) - 1:
            prev, curr, next = flowerbed[i - 1], flowerbed[i], flowerbed[i + 1]

            if prev == curr == next == 0:
                n -= 1
                flowerbed[i] = 1

            i += 1

        return n == 0
