class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        end=len(nums)
        count=0
        count2=0
        while count2<end:
            if nums[count]==0:
                nums.insert(0,nums.pop(count))
                
            elif nums[count] ==2:
                nums.append(nums.pop(count))
                count-=1
            count+=1                
            count2+=1


#url: https://leetcode.com/problems/sort-colors/
