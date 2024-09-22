# 735. Asteroid Collision


from typing import List


class Solution:

    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            while stack and stack[-1] > 0 and asteroid < 0:
                if stack[-1] + asteroid < 0:
                    stack.pop()
                elif stack[-1] + asteroid > 0:
                    break
                else:
                    stack.pop()
                    break
            else:
                stack.append(asteroid)
        return stack


result = Solution()
asteroids = [5, 10, -5]
output = result.asteroidCollision(asteroids)
print(f"Output: {output}")
expected = [5, 10]
if output == expected:
    print("Test passed successfully!")
else:
    print("Test failed!")
