# 605. Can Place Flowers


from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowers_planted = 0
        length = len(flowerbed)

        for i in range(length):
            left = flowerbed[i - 1] if i - 1 >= 0 else 0
            right = flowerbed[i + 1] if i + 1 < length else 0
            if left == right == flowerbed[i] == 0:
                flowers_planted += 1
                flowerbed[i] = 1
            if flowers_planted >= n:
                return True

        return False


result = Solution()
flowerbed = [1, 0, 0, 0, 1, 0, 0, 0, 0, 1]
n = 3
output = result.canPlaceFlowers(flowerbed, n)
print(f"Output: {output}")
expected = True
if output == expected:
    print("Test passed successfully!")
else:
    print("Test failed!")
