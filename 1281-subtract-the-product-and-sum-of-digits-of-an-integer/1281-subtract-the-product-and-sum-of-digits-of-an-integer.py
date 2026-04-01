class Solution(object):
    def subtractProductAndSum(self, n):
        p = 1
        s = 0
        
        for i in str(n):
            digit = int(i)
            p *= digit
            s += digit
        
        return p - s