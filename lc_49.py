# 49. Group Anagrams


from typing import List
from utils import are_equal_arrays
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)

        for string in strs:
            key = "".join(sorted(string))
            anagram_map[key].append(string)

        return anagram_map.values()


result = Solution()
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
output = result.groupAnagrams(strs)
print(f"Output: {output}")
expected = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
if are_equal_arrays(expected, output):
    print("Test passed successfully!")
else:
    print("Test failed!")

