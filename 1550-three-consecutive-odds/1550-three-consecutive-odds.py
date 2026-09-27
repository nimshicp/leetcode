class Solution(object):
    def threeConsecutiveOdds(self, arr):
      consecutive=0
      for i  in arr:
        if i%2!=0:
          consecutive+=1
          if consecutive==3:
            return True
        else:
          consecutive=0  
      return False    
          
         
           
s=Solution()
print(s.threeConsecutiveOdds([2,6,4,1]))