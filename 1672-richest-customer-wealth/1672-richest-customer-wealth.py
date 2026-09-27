class Solution(object):
    def maximumWealth(self, accounts):
      max=0
      
      for i in accounts:
        count=0
        for j in range(len(i)):
          count+=i[j]
        if count>max:
          max=count
      return max

s=Solution()
print(s.maximumWealth([[2,8,7],[7,1,3],[1,9,5]]))