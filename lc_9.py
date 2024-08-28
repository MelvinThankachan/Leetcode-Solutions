# 9. Palindrome Number


class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        n = len(x)
        for i in range(n//2):
            if x[i] != x[n-i-1]:
                return False
        return True


result = Solution()
x = -121
output = result.isPalindrome(x)
print(output)
expected = True
if output == expected:
    print("Test passed successfully!")
else:
    print("Test failed!")
