class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        count=0 #count current index

        for i in range(len(nums)):
            
            temp=nums.pop(0) #pop first element and store to temp
            if target-temp in nums: #check if target-temp is inside nums
                return [count,count+nums.index(target-temp)+1] #return current index and target-temp's index

            count+=1
            
#url:https://leetcode.com/problems/two-sum/
