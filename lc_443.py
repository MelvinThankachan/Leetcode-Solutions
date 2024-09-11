# 443. String Compression


from typing import List


class Solution:

    # My solution
    def compress(self, chars: List[str]) -> int:
        current_char = chars[0]
        current_count = 0
        j = 0
        n = len(chars)

        for char in chars:
            if char != current_char:
                current_char = char
                j += 1
                if current_count > 1:
                    count = str(current_count)
                    for digit in count:
                        chars[j] = digit
                        j += 1
                current_count = 1
                chars[j] = char
            else:
                current_count += 1
        else:
            j += 1
            if current_count > 1:
                count = str(current_count)
                for digit in count:
                    chars[j] = digit
                    j += 1
        while j < n:
            chars.pop()
            n -= 1
        return chars

    # Best Solution
    def compress(self, chars: List[str]) -> int:
        write = 0
        read = 0
        n = len(chars)

        while read < n:
            char = chars[read]
            count = 0
            # Counting the number of occurrences of the current character
            while read < n and chars[read] == char:
                read += 1
                count += 1
            # Writing the character to the array
            chars[write] = char
            write += 1
            # Writing the count as well
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        return write


result = Solution()
chars = ["a", "a", "b", "b", "c", "c", "c"]
extraCandies = 3
output = result.compress(chars)
print(f"Output: {output}")
expected = ["a", "2", "b", "2", "c", "3"]
if output == expected:
    print("Test passed successfully!")
else:
    print("Test failed!")
