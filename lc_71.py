# 71. Simplify Path


class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        files = path.split("/")
        for file_name in files:
            if file_name == "..":
                if stack:
                    stack.pop()
            elif file_name and file_name != ".":
                stack.append(file_name)

        return "/" + "/".join(stack)


result = Solution()
path = "/.../a/../b/c/../d/./"
output = result.simplifyPath(path)
print(f"Output: {output}")
expected = "/.../b/d"
if output == expected:
    print("Test passed successfully!")
else:
    print("Test failed!")
