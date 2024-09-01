# 1431. Kids With the Greatest Number of Candies

from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = max(candies)
        return [candy + extraCandies >= max_candy for candy in candies]


result = Solution()
candies = [2, 3, 5, 1, 3]
extraCandies = 3
output = result.kidsWithCandies(candies, extraCandies)
print(f"Output: {output}")
expected = [True, True, True, False, True]
if output == expected:
    print("Test passed successfully!")
else:
    print("Test failed!")

