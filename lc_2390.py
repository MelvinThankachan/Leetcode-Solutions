# 2390. Removing Stars From a String


from collections import deque


class Solution:
    def removeStars(self, s: str) -> str:
        stack = deque()

        for char in s:
            if char == "*":
                stack.pop()
            else:
                stack.append(char)

        return "".join(stack)


result = Solution()
s = "leet**cod*e"
output = result.removeStars(s)
print(f"Output: {output}")
expected = "lecoe"
if output == expected:
    print("Test passed successfully!")
else:
    print("Test failed!")
