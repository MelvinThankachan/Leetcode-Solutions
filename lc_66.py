# 66. Plus One


class Solution(object):
    def plusOne(self, digits):
        i = len(digits) - 1
        while i >= 0:
            if digits[i] == 9:
                digits[i] = 0
                i -= 1
            else:
                digits[i] += 1
                break
        if i < 0:
            digits.insert(0, 1)
        return digits
