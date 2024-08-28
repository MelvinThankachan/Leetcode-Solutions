class Solution(object):
    def maxProfit(self, prices):
        no_of_prices = len(prices)
        max_profit = 0
        for i in range(no_of_prices - 1):
            if prices[i] < prices[i + 1]:
                max_profit += prices[i + 1] - prices[i]
        return max_profit


result = Solution()
prices = [1, 2, 3, 4, 5]
output = result.maxProfit(prices)
print(output)
expected = 4
if output == expected:
    print("Test passed successfully!")
else:
    print("Test failed!")
