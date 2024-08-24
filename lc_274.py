class Solution(object):
    def hIndex(self, citations):
        h_index = len(citations)
        citations.sort()

        for i in citations:
            if i < h_index:
                h_index -= 1
            
            if h_index <= i:
                break
        
        return h_index


result = Solution()
citations = [3,0,6,1,5]
output = result.hIndex(citations)
print("output", output)
expected = 3
if output == expected:
    print("Test passed successfully!")
