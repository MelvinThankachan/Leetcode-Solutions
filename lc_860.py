from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = 0
        tens = 0
        for bill in bills:
            if bill == 5:
                fives += 1
            elif bill == 10:
                fives -= 1
                tens += 1
            elif tens > 0:
                tens -= 1
                fives -= 1
            else:
                fives -= 3

            if fives < 0:
                return False

        return True


result = Solution()
bills = [5, 5, 10, 10, 20]
output = result.lemonadeChange(bills)
print("output", output)
expected = False
if output == expected:
    print("Test passed successfully!")
else:
    print("Test failed!")

