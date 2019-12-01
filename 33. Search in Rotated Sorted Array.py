class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if nums==[]:
            return -1
        
        start=0
        end=len(nums)-1

        while True:
            if nums[start]==target:
                return start
            if nums[end]==target:
                return end
            if end<=start:
                return -1
            end-=1
            start+=1

        return -1
        
#url: https://leetcode.com/problems/search-in-rotated-sorted-array/
