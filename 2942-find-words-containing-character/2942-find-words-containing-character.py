class Solution(object):
    def findWordsContaining(self, words, x):
      arr=[]
      for a,i in enumerate(words):
          if x in i :
            arr.append(a)
      return arr
      
        
s=Solution()  
print(s.findWordsContaining(["leet","code"], "e"))

              