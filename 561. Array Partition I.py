class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        ans=[nums[i] for i in range(len(nums)) if i%2==0]
        return sum(ans)
        
#url: https://leetcode.com/problems/array-partition-i/
