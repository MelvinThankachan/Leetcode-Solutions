# 1071. Greatest Common Divisor of Strings


from math import gcd


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        return str1[: gcd(len(str1), len(str2))]


result = Solution()
str1 = "ABCABC"
str2 = "ABC"
output = result.gcdOfStrings(str1, str2)
print(f"Output: {output}")
expected = "ABC"
if output == expected:
    print("Test passed successfully!")
else:
    print("Test failed!")
