class Solution(object):
    def decodeString(self, s):  # a22[b3[c]d]e
        stack = []
        curr_str = ''
        curr_digit = 0

        for _s in s:
            if _s.isdigit():
                curr_digit = curr_digit * 10 + int(_s)
            elif _s == '[':
                stack.append((curr_str, curr_digit))
                curr_str = ''
                curr_digit = 0
            elif _s == ']':
                prev_str, prev_digit = stack.pop()
                curr_str = prev_str + curr_str * prev_digit
            else:
                curr_str += _s

        return curr_str
