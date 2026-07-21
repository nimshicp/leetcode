class Solution(object):
    def containsDuplicate(self, nums):
    
        d = {}

        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        for k in d.values():
            if k > 1:
                return True

        return False
            