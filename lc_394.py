# 394. Decode String


class Solution:
    # My Solution
    def decodeString(self, s: str) -> str:
        n = len(s)
        nums = []
        chars = [""]

        i = 0
        while i < n:
            c = s[i]
            if c.isdigit():
                nums.append("")
                while s[i].isdigit():
                    nums[-1] += s[i]
                    i += 1
                continue
            elif c == "[":
                chars.append("")
            elif c.isalpha():
                chars[-1] += c
            elif c == "]":
                char = chars.pop() * int(nums.pop())
                chars[-1] += char
            i += 1

        return chars[0]

    # Best Solution
    def decodeString(self, s: str) -> str:
        stack = []
        current_num = 0
        current_str = ""

        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            elif char == "[":
                stack.append((current_str, current_num))
                current_str, current_num = "", 0
            elif char == "]":
                last_str, num = stack.pop()
                current_str = last_str + (current_str * num)
            else:
                current_str += char
        return current_str

    # Another Solution
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            if char != "]":
                stack.append(char)
                continue

            inner_string = ""
            while stack and stack[-1] != "[":
                inner_string = stack.pop() + inner_string
            stack.pop()

            multiplier_str = ""
            while stack and stack[-1].isdigit():
                multiplier_str = stack.pop() + multiplier_str
            multiplier = int(multiplier_str)
            stack.append(inner_string * multiplier)

        return "".join(stack)


result = Solution()
s = "3[a2[c]]"
output = result.decodeString(s)
print(f"Output: {output}")
expected = "accaccacc"
if output == expected:
    print("Test passed successfully!")
else:
    print("Test failed!")
