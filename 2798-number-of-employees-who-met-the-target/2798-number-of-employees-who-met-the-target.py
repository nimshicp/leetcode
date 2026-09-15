class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours,target):
      count=0
     
      for i in hours:
        if i>=target:
          count+=1
      return count    
          

      
s=Solution()
print(s. numberOfEmployeesWhoMetTarget([2,5,4,1,3],2))
          
          