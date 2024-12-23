class Solution(object):
    def asteroidCollision(self, asteroids):
        result = []

        for asteroid in asteroids:
            if asteroid < 0:
                is_destroyed = False

                while result and result[-1] > 0 and not is_destroyed:
                    if result[-1] > -asteroid:
                        is_destroyed = True
                    elif result[-1] == -asteroid:
                        result.pop()
                        is_destroyed = True
                    else:
                        result.pop()

                if not is_destroyed:
                    result.append(asteroid)
            else:
                result.append(asteroid)

        return result
