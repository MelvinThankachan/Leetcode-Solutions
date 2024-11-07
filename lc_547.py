# 547. Number of Provinces


from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(i):
            visited[i] = True
            for j in range(n):
                if isConnected[i][j] == 1 and not visited[j]:
                    dfs(j)

        n = len(isConnected)
        visited = [False] * n
        provinces = 0

        for i in range(n):
            if not visited[i]:
                provinces += 1
                dfs(i)

        return provinces


result = Solution()
isConnected = [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]
output = result.findCircleNum(isConnected)
print(f"Output: {output}")
expected = 1
if output == expected:
    print("Test passed successfully!")
else:
    print("Test failed!")
