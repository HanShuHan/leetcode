class Solution(object):
    def dailyTemperatures(self, temperatures):
        temperatures_len = len(temperatures)

        if len(temperatures) == 1:
            return [0]

        result = [0] * temperatures_len

        stack = [0]
        for i in range(1, temperatures_len):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                index = stack.pop()

                result[index] = i - index
            stack.append(i)

        return result


        # stack = []
        #
        # for i in range(temperatures_len - 1):
        #     if temperatures[i] < temperatures[i + 1]:
        #         result[i] = 1
        #
        #         while stack and stack[-1][1] < temperatures[i + 1]:
        #             index, temp = stack.pop()
        #             result[index] = i + 1 - index
        #     else:
        #         stack.append((i, temperatures[i]))
        #
        # return result
