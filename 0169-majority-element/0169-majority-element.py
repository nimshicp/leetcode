class Solution(object):
    def majorityElement(self, nums):
        d={}
        n=len(nums)//2
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for k,v in d.items():
            if v >n:
                return k
s=Solution()
print(s.majorityElement([2,2,3,3,3,2,3]))