class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        ind=len(digits)-1
        
        while True:
            digits[ind]=digits[ind]+1
            
            if digits[ind]==10:
                if ind==0:
                    digits[ind]=0
                    digits.insert(0,1)
                    break
                digits[ind]=0  
                ind-=1                              
            else:
                break
            
        
        return digits
        
#url: https://leetcode.com/problems/plus-one/
