class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        ans=[0 for i in range(len(nums))]
        temp=0
        temp2=0
        for num in nums:
            for n in nums:
                if n < num:
                    temp+=1
            ans[temp2]=temp
            temp=0
            temp2+=1
            
        return ans
        
#url:https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
