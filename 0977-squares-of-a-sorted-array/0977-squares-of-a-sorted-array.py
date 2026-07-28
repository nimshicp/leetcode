


class Solution(object):
    def sortedSquares(self, nums):
        result=[]
        for i in nums:
            result.append(i*i)
        return sorted(result)   
            
        
        
s=Solution()
print(s.sortedSquares([-7,-3,2,3,11]))