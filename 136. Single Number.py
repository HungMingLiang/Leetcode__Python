class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            num=nums.pop(0)
            if num in nums:
			          nums.remove(num)
            else:
                return num


#url: https://leetcode.com/problems/single-number/
