# 2678. Number of Senior Citizens


class Solution:
    def countSeniors(self, details):
        seniors = 0
        for detail in details:
            age = int(detail[11:13])
            if age > 60:
                seniors += 1
        return seniors


result = Solution()
details = ["7868190130M7522", "5303914400F9211", "9273338290F4010"]
output = result.countSeniors(details)
print(output)
expected = 2
if output == expected:
    print("jayichu mone!")
