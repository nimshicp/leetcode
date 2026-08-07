class Solution(object):
    def maxArea(self, height):
        left=0
        right=len(height)-1
        result=0
        while left<right:
            width=right-left
            h=min(height[left],height[right])
            area=width*h
            if area>=result:
                result=area
                
            if height[left]< height[right]:
                left+=1
            else:
                right-=1
        return result        
                
s=Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))