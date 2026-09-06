class Solution(object):
    def firstUniqChar(self, s):
      
      d={}
      for i in s:
        if i in d:
          d[i]+=1
        else:
          d[i]=1
      for index, j in enumerate(s):
        if d[j]==1:
          return index
    
      return -1
      
s=Solution()
print(s.firstUniqChar('aabbb'))

          

