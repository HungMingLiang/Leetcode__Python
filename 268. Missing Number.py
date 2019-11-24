class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        tar=0
        for num in nums:
            if num!=tar:
                return tar
            tar+=1
        return tar
        
#url: https://leetcode.com/problems/missing-number/
