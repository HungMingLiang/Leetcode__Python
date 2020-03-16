class Solution:
    def numberOfSteps (self, num: int) -> int:
        count=0
        
        while True:
            
            if num==1:
                break
            
            if num%2==0:
                num=num/2
                count+=1
            else:
                num=num-1
                count+=1
                
        return count+1
        
#url:https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
