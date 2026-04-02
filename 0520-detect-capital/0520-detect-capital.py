class Solution(object):
    def detectCapitalUse(self, word):
        w1=word.upper()
        w2=word.lower()
        w3=word[0].upper() + word[1:].lower()
        if word == w1 or word == w2 or word == w3:
            return True
        else:
            return False    
            
        