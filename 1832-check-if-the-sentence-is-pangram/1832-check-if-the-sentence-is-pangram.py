class Solution(object):
    def checkIfPangram(self, sentence):
        sentence=sentence.lower()
        for char in "abcdefghijklmnopqrstuvwxyz":
          if char not in sentence:
            return False
        return True    
s=Solution()
print(s.checkIfPangram("thequickbrownfoxjumpsoverthelaydog"))
      