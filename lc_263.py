from math import sqrt, ceil


class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        for prime in [2, 3, 5]:
            while n % prime == 0:
                n /= prime

        return n == 1


result = Solution()
n = 347826
output = result.isUgly(n)
print(f"Output: {output}")
expected = True
if output == expected:
    print("Test passed successfully!")
else:
    print("Test failed!")
