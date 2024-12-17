class Solution(object):
    def asteroidCollision(self, asteroids):
        stack = []

        for asteroid in asteroids:
            is_destroyed = False
            while stack and asteroid < 0 < stack[-1]:
                if stack[-1] > -asteroid:
                    is_destroyed = True
                    break
                elif stack[-1] == -asteroid:
                    stack.pop()
                    is_destroyed = True
                    break
                else:
                    stack.pop()

            if not is_destroyed:
                stack.append(asteroid)

        return stack

