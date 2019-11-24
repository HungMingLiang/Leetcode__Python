class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        return not len(nums) == len(set(nums)) #check if the set have same length
        
# url: https://leetcode.com/problems/contains-duplicate/
