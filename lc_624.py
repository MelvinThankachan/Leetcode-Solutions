from typing import List


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        minimum = arrays[0][0]
        maximum = arrays[0][-1]
        distance = 0

        for array in arrays[1:]:
            array_min = array[0]
            array_max = array[-1]
            distance = max(distance, maximum - array_min, array_max - minimum)
            minimum = min(array_min, minimum)
            maximum = max(array_max, maximum)

        return distance


result = Solution()
arrays = [[1, 5], [3, 4]]
output = result.maxDistance(arrays)
print("output", output)
expected = 3
if output == expected:
    print("jayichu mone!")
