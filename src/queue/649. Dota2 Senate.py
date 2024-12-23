from collections import deque


class Solution(object):
    def predictPartyVictory(self, senate):
        radiant = deque()
        dire = deque()
        n = len(senate)

        for i in range(n):
            if senate[i] == 'R':
                radiant.append(i)
            elif senate[i] == 'D':
                dire.append(i)

        while radiant and dire:
            r = radiant.popleft()
            d = dire.popleft()

            if r < d:
                radiant.append(r + n)
            else:
                dire.append(d + n)

        return 'Radiant' if radiant else 'Dire'
