from typing import List, Set


class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        """
        Building the adjacency list representation of the graph.
        Each variable is a node, and each equation is a bi-directional
        weighted edge between variables.
        Example: a/b=2.0 => a->b (2.0), b->a (0.5)
        """
        graph = {}
        for (a, b), value in zip(equations, values):
            if a not in graph:
                graph[a] = {}
            if b not in graph:
                graph[b] = {}
            graph[a][b] = value
            graph[b][a] = 1 / value

        def dfs(src: str, dst: str, visited: Set[str]) -> float:
            """
            Depth-First Search to find the result of src / dst.
            If path exists, multiply the weights along the path.
            Use visited set to avoid cycles in the graph.
            """
            if src not in graph or dst not in graph:
                return -1.0
            if src == dst:
                return 1.0

            visited.add(src)
            for neighbor, value in graph[src].items():
                if neighbor in visited:
                    continue
                ans = dfs(neighbor, dst, visited)
                if ans != -1.0:
                    return ans * value
            return -1.0

        results = []
        for query in queries:
            results.append(dfs(query[0], query[1], set()))
        return results


# Example usage and validation
result = Solution()
equations = [["x1", "x4"], ["x2", "x3"], ["x1", "x2"], ["x2", "x5"]]
values = [3.0, 0.5, 3.4, 5.6]
queries = [
    ["x1", "x5"],
    ["x4", "x5"],
    ["x1", "x3"],
    ["x5", "x5"],
    ["x5", "x1"],
    ["x3", "x4"],
    ["x4", "x3"],
    ["x6", "x6"],
    ["x0", "x0"],
]
output = result.calcEquation(equations, values, queries)
print(f"Output: {output}")
expected = [
    19.04000,
    6.34667,
    1.70000,
    1.00000,
    0.05252,
    1.76471,
    0.56667,
    -1.00000,
    -1.00000,
]
if output == expected:
    print("Test passed successfully!")
else:
    print("Test failed!")
