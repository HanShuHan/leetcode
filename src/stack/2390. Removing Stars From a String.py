class Solution(object):
    def removeStars(self, s):
        stack = []

        for _s in s:
            if _s == '*' and stack[-1] != '*':
                stack.pop()
            else:
                stack.append(_s)

        return ''.join(stack)
