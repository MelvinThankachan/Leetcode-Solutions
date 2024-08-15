from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = ten = 0
        for i in bills:
            if i == 5:
                five += 1
            elif i == 10:
                five, ten = five - 1, ten + 1
            elif ten > 0:
                five, ten = five - 1, ten - 1
            else:
                five -= 3
            if five < 0:
                return False
        return True


result = Solution()
bills = [5,5,10,10,20]
output = result.lemonadeChange(bills)
print("output", output)
expected = False
if output == expected:
    print("jayichu mone!")