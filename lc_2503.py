# 2053. Kth Distinct String in an Array

from typing import List
from collections import Counter


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        strings_map = {}
        for string in arr:
            if string not in strings_map:
                strings_map[string] = 1
            else:
                strings_map[string] += 1

        distinct_strings = []
        for string in strings_map.keys():
            if strings_map[string] == 1:
                distinct_strings.append(string)

        result = ""
        if k <= len(distinct_strings):
            result += distinct_strings[k - 1]
        return result

    def kthDistinct(self, arr: List[str], k: int) -> str:
        strings_map = Counter(arr)
        for i in arr:
            if strings_map[i] == 1:
                k -= 1
            if k == 0:
                return i
        return ""


result = Solution()
arr = ["d", "b", "c", "b", "c", "a"]
k = 2
output = result.kthDistinct(arr, k)
print(f"Output: {output}")
expected = "a"
if output == expected:
    print("Test passed successfully!")
else:
    print("Test failed!")

