class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        i=0
        j=0
        count1=0
        count2=0

        while i< len(nums1):
            if nums1[i] in nums2:
                count1+=1
            i+=1    
        while j< len(nums2):
            if nums2[j] in nums1:
                count2+=1
            j+=1
        return [count1,count2]        



            

        