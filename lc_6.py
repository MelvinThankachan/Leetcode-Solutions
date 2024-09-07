class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1: return s

        n = len(s)
        rows = ["" for i in range(numRows)]
        i = 0
        index = 0
        forward = True
        while i < n:
            rows[index] += s[i]

            if index == numRows - 1:
                forward = False
            if index == 0:
                forward = True

            if forward:
                index += 1
            else:
                index -= 1

            i += 1

        result = ""
        for row in rows:
            result += row

        return result


result = Solution()
s = "MELVINISGREAT"
numRows = 2
output = result.convert(s, numRows)
print(f"Output: {output}")
expected_output = "PAHNAPLSIIGYIR"
if output == expected_output:
    print("Test passed successfully!")
else:
    print("Test failed!")
