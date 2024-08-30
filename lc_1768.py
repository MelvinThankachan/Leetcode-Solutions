# 1768. Merge Strings Alternately


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n_word1 = len(word1)
        n_word2 = len(word2)
        result = ""
        index = 0

        while index < n_word1:
            result += word1[index]
            result += word2[index]
            index += 1
            if index >= n_word1:
                result += word2[index:n_word2]
                break
            elif index >= n_word2:
                result += word1[index:n_word1]
                break

        return result


result = Solution()
word1 = "abc"
word2 = "pqr"
output = result.mergeAlternately(word1, word2)
print("output", output)
expected = "apbqcr"
if output == expected:
    print("Test passed successfully!")
else:
    print("Test failed!")
