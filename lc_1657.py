# 1657. Determine if Two Strings Are Close


from collections import defaultdict, Counter


class Solution:
    # My Solution
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        count_map_1 = defaultdict(int)
        count_map_2 = defaultdict(int)
        for char in word1:
            count_map_1[char] += 1
        for char in word2:
            count_map_2[char] += 1

        chars_1 = sorted(count_map_1.keys())
        chars_2 = sorted(count_map_2.keys())
        counts_1 = sorted(count_map_1.values())
        counts_2 = sorted(count_map_2.values())

        return chars_1 == chars_2 and counts_1 == counts_2

    # Another Way
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        count1 = Counter(word1)
        count2 = Counter(word2)

        if set(count1.keys()) != set(count2.keys()):
            return False

        return sorted(count1.values()) == sorted(count2.values())


result = Solution()
word1 = "cabbba"
word2 = "abbccc"
output = result.closeStrings(word1, word2)
print(f"Output: {output}")
expected = True
if output == expected:
    print("Test passed successfully!")
else:
    print("Test failed!")
