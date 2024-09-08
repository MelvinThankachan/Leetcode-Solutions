# 1456. Maximum Number of Vowels in a Substring of Given Length


class Solution:
    # My Solution
    def maxVowels(self, s: str, k: int) -> int:
        VOWELS = {"a", "e", "i", "o", "u"}
        n = len(s)
        left = 0
        right = k
        vowels = 0
        for char in s[left:right]:
            if char in VOWELS:
                vowels += 1
        max_vowels = vowels

        while right < n:
            if s[left] in VOWELS:
                vowels -= 1
            if s[right] in VOWELS:
                vowels += 1
            max_vowels = max(vowels, max_vowels)
            left += 1
            right += 1

        return max_vowels
    

    # Another Solution
    def maxVowels(self, s: str, k: int) -> int:
        VOWELS = {"a", "e", "i", "o", "u"}
        vowels_count = max_vowels = 0

        for i, char in enumerate(s):
            if char in VOWELS:
                vowels_count += 1
            if i >= k and s[i-k] in VOWELS:
                vowels_count -= 1
            max_vowels = max(vowels_count, max_vowels)

        return max_vowels

result = Solution()
s = "abciiidef"
k = 3
output = result.maxVowels(s, k)
print(f"Output: {output}")
expected = 3
if output == expected:
    print("Test passed successfully!")
else:
    print("Test failed!")
