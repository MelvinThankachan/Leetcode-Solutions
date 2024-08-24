# 564. Find the Closest Palindrome


class Solution:
    def nearestPalindromic(self, n: str) -> str:
        n_length = len(n)


result = Solution()
n = "123"
output = result.nearestPalindromic(n)
print("output", output)
expected = "0"
if output == expected:
    print("jayichu mone!")
