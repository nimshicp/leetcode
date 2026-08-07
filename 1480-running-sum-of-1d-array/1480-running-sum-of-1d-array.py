class Solution(object):
    def runningSum(self, nums):
        array=[]
        result=0
        for i in nums:
            result=result+i
            array.append(result)
        return array    
        
s=Solution()
print(s.runningSum([1,2,3,4]))
            