class Solution(object):
    def mostWordsFound(self, sentences):
      max=0
      for i in sentences:
        count=len(i.split())
        if count>max:
          max=count
      return max    
          
        
          
        
s=Solution()
print(s.mostWordsFound(["alice and bob love leetcode", "i think so too", "this is great thanks very much"]))









