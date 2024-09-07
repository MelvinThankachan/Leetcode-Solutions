class Solution(object):
    def fullJustify(self, words, maxWidth):
        length = 0
        start = 0
        result = []
        for i, word in enumerate(words):
            word_lenth = len(word)
            length += word_lenth
            
            if length + word_lenth > maxWidth:
                start = i
                spaces = maxWidth - length
                



result = Solution()
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
output = result.fullJustify(words, maxWidth)
print(f"Output: {output}")
expected_output = ["This    is    an","example  of text","justification.  "]
if output == expected_output:
    print("Test passed successfully!")
else:
    print("Test failed!")