class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0 #return value
        count = 0 #max count

        for i in range(len(nums)):
            if nums == []: #if empty break
                break
            jj = nums[0]
            countN=nums.count(jj) #count first element in nums
            if countN>count:
                count=countN
                ans=jj
            nums=[x for x in nums if x!=jj] #delete all number are first element

        return ans

#url:https://leetcode.com/problems/majority-element/
