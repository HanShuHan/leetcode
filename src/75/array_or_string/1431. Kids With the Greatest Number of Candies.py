class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        candies_len = len(candies)
        max_candy = max(candies)
        result = [False] * candies_len

        for i in range(candies_len):
            if candies[i] + extraCandies >= max_candy:
                result[i] = True

        return result
