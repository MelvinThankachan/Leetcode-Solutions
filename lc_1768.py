# 1768. Merge Strings Alternately


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n_word1 = len(word1)
        n_word2 = len(word2)
        result = []
        index = 0
        while index < n_word1 or index < n_word2:
            if index < n_word1:
                result.append(word1[index])
            if index < n_word2:
                result.append(word2[index])
            index += 1

        return "".join(result)


result = Solution()
word1 = "abc"
word2 = "pqr"
output = result.mergeAlternately(word1, word2)
print(f"Output: {output}")
expected = "apbqcr"
if output == expected:
    print("Test passed successfully!")
else:
    print("Test failed!")
