# 1732. Find the Highest Altitude


from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt = max_alt = 0
        for altitude in gain:
            alt += altitude
            if alt > max_alt:
                max_alt = alt

        return max_alt


result = Solution()
gain = [-4, -3, -2, -1, 4, 3, 2]
output = result.largestAltitude(gain)
print(f"Output: {output}")
expected = 0
if output == expected:
    print("Test passed successfully!")
else:
    print("Test failed!")
