class Solution(object):
    def twoSum(self, numbers, target):
        left =  0
        right = len(numbers) - 1
        while numbers[left] + numbers[right] != target:
            total = numbers[left] + numbers[right]
            if total < target:
                left += 1
            elif total > target:
                right -=1
        return [left + 1,right + 1]


result = Solution()
numbers = [2,7,11,15]
target = 9
output = result.twoSum(numbers, target)
print(f"Output: {output}")
expected = [1, 2]
if output == expected:
    print("Test passed successfully!")
else:
    print("Test failed!")

