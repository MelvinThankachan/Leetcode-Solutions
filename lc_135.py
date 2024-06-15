"""

There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.

"""

import time


class Solution(object):

    def candy(self, ratings):
        n = len(ratings)
        candy_list = [1] * n

        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candy_list[i] = candy_list[i - 1] + 1
        
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candy_list[i] = max(candy_list[i], candy_list[i+1]+1)
        
        return sum(candy_list)


result = Solution()
ratings = [1, 3, 4, 5, 2]
output = result.candy(ratings)
print(output)
expected_output = 11
if output == expected_output:
    print("Jayichu mwone!")
