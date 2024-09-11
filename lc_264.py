class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly_numbers = [1]
        pointer_2 = pointer_3 = pointer_5 = 0

        for _ in range(1, n):
            value_2 = ugly_numbers[pointer_2] * 2
            value_3 = ugly_numbers[pointer_3] * 3
            value_5 = ugly_numbers[pointer_5] * 5
            min_value = min(value_2, value_3, value_5)
            ugly_numbers.append(min_value)
            if value_2 == min_value:
                pointer_2 += 1
            if value_3 == min_value:
                pointer_3 += 1
            if value_5 == min_value:
                pointer_5 += 1

        return ugly_numbers[-1]


result = Solution()
n = 10
output = result.nthUglyNumber(n)
print(f"Output: {output}")
expected = 12
if output == expected:
    print("Test passed successfully!")
else:
    print("Test failed!")

