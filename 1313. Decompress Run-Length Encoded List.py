class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        
        ans=[]
        
        times=int(len(nums)/2)
        
        for i in range(times):
            x=nums.pop(0)
            y=nums.pop(0)
            
            for i in range(x):
                ans.append(y)
                
        
        return ans
        
#url:https://leetcode.com/problems/decompress-run-length-encoded-list/
