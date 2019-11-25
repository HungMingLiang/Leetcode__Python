class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if nums[0]<=nums[len(nums)-1]:
            return nums[0]
        
        ind=int(len(nums)/2)
        
        while True:
            if nums[ind]>nums[0]:
                ind+=1
            elif nums[ind]<nums[0]:
                if nums[ind]<nums[ind-1]:
                    return nums[ind]
                else:
                    ind-=1
        
            
#url: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
