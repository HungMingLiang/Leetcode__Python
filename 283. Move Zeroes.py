class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count=nums.count(0) #count how many zero
        for i in range(count):
            nums.remove(0) #remove one zero 
            nums.append(0) #append one zero to last

#url: https://leetcode.com/problems/move-zeroes/
