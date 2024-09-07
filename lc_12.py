class Solution(object):
    def intToRoman(self, num):
        roman_list = [
            ("M", 1000),
            ("CM", 900 ),
            ("D", 500),
            ("CD", 400),
            ("C", 100),
            ("XC", 90),
            ("L", 50),
            ("XL", 40),
            ("X", 10),
            ("IX", 9),
            ("V", 5),
            ("IV", 4),
            ("I", 1),
        ]
        result = ""
        n = len(roman_list)

        for roman, digit in roman_list:
            mul = num // digit
            if mul:
                result += roman * mul
                num %= digit
        
        return result


result = Solution()
num = 3749
output = result.intToRoman(num)
print(f"Output: {output}")
expected_output = "MMMDCCXLIX"
if output == expected_output:
    print("Test passed successfully!")
else:
    print("Test failed!")
