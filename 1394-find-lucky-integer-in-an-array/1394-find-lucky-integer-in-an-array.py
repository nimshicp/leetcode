class Solution(object):
    def findLucky(self, arr):
        d={}
        h=0
        for i in arr:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for k,v in d.items():
            if k == v and k > h:
                h=k
        if h ==0 :
            return -1
        else:
            return h
                

s=Solution()
print(s.findLucky([2,2,3,3,3]))
            