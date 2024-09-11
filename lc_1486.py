# 1486. XOR Operation in an Array


class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        result = 0
        for i in range(n):
            result ^= start + 2 * i

        return result


result = Solution()
n = 5
start = 0
output = result.xorOperation(n, start)
print(f"Output: {output}")
expected = 8
if output == expected:
    print("Test passed successfully!")
else:
    print("Test failed!")

