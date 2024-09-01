# 345. Reverse Vowels of a String


class Solution:
    def reverseVowels(self, s: str) -> str:
        VOWELS = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        s_list = []
        indices = []
        vowels = []

        for i, char in enumerate(s):
            s_list.append(char)
            if char in VOWELS:
                indices.append(i)
                vowels.append(char)

        vowels.reverse()
        for i, vowel in enumerate(vowels):
            s_list[indices[i]] = vowel

        return "".join(s_list)


result = Solution()
s = "leetcode"
output = result.reverseVowels(s)
print(f"Output: {output}")
expected = "leotcede"
if output == expected:
    print("Test passed successfully!")
else:
    print("Test failed!")
