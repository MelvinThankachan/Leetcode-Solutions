# 875. Koko Eating Bananas
import math


class Solution(object):
    def minEatingSpeed(self, piles, h):
        l = 1
        r = max(piles)
        while l < r:
            k = (l + r) // 2
            hrs = 0
            for pile in piles:
                hrs += math.ceil(pile / k)
            if hrs > h:
                l = k + 1
            else:
                r = k
        return l


result = Solution()
piles = [3, 6, 7, 11]
h = 8
output = result.minEatingSpeed(piles, h)
print(output)
expected = 4
if output == expected:
    print("jayichu mone!")
