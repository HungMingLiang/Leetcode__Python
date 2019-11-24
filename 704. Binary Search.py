class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ind=int(len(nums)/2)
        ind2=int(ind/2)
        for i in range(len(nums)):

            if ind2==0:
                ind2+=1
            if ind==len(nums):
                break
            if nums[ind]==target:
                return ind
            elif nums[ind]<target:
                ind=ind+ind2
                ind2=int(ind2/2)
            else:
                ind=ind-ind2
                ind2=int(ind2/2)
        
        return -1

#url:https://leetcode.com/problems/binary-search/
