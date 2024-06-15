class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        if sum(gas) < sum(cost):
            return -1

        tank, start, length = 0, 0, len(gas)

        for i in range(length):
            tank += gas[i] - cost[i]

            if tank < 0:
                start = i + 1
                tank = 0

        return start


result = Solution()
gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
output = result.canCompleteCircuit(gas, cost)
print(output)
expected_output = 3
if output == expected_output:
    print("Jayichu mwone!")
