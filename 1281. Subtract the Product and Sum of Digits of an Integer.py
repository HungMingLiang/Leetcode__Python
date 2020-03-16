class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        

        nL=[int(i) for i in str(n)]
        
        temp1=int(nL[0])
        temp2=int(nL[0])
        
        for i in range(1,len(nL)):
            temp1=temp1*nL[i]
            temp2=temp2+nL[i]
            
        return temp1-temp2
        
#url:https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
