class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxW=0
        
        i=0
        j=len(height)-1
        
        while i<j:
            if height[i]<height[j]:
                temp=height[i]*(j-i)
                i+=1
            else:
                temp=height[j]*(j-i)
                j-=1
                
            if temp>maxW:
                maxW=temp
                
        return maxW
        
#url: https://leetcode.com/problems/container-with-most-water/
