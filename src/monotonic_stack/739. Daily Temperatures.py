class Solution(object):
    def dailyTemperatures(self, temperatures):
        list_size = len(temperatures)
        if list_size == 1:
            return [0]

        result = [0] * list_size
        stack = [0]
        for i in range(1, list_size):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                result[prev_index] = i - prev_index
            stack.append(i)

        return result
