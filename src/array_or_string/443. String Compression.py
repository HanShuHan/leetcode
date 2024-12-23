class Solution(object):

    def __init__(self):
        self.write_idx = 0

    def rewrite(self, curr_char, count, chars):
        chars[self.write_idx] = curr_char
        self.write_idx += 1

        if count > 1:
            for digit in str(count):
                chars[self.write_idx] = digit
                self.write_idx += 1

    def compress(self, chars):
        count = 1
        curr_char = chars[0]

        for i in range(1, len(chars)):
            if chars[i] == curr_char:
                count += 1
            else:
                self.rewrite(curr_char, count, chars)
                curr_char = chars[i]
                count = 1

        self.rewrite(curr_char, count, chars)

        return self.write_idx
