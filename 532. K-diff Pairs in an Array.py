class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        lList=[]
        nums.sort()
        if k<0:
            return 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[j]-nums[i]==k:
                    lList.append([nums[i],nums[j]])
                if nums[j]-nums[i]>k:
                    break

        s=set(tuple(l) for l in lList)
        return len(s)
        
#url: https://leetcode.com/problems/k-diff-pairs-in-an-array/
