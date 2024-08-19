from math import sqrt, ceil


class Solution:
    def isUgly(self, n: int) -> bool:
        # if n <= 0:
        #     return False

        # while n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
        #     if n % 2 == 0:
        #         n /= 2
        #     if n % 3 == 0:
        #         n /= 3
        #     if n % 5 == 0:
        #         n /= 5

        # return n == 1


        if n % 2 == 0:
            n /= 2
        if n % 3 == 0:
            n /= 3
        if n % 5 == 0:
            n /= 5
            
        if n == 1:
            return True
        else:
            return False

        return self.isUgly(n)


result = Solution()
n = 347826
output = result.isUgly(n)
print("output", output)
expected = True
if output == expected:
    print("jayichu mone!")
