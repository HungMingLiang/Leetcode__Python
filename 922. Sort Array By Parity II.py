class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        
        e=[a for a in A if a%2==0]
        o=[a for a in A if a%2==1]
        ans=[]
        for i in range(len(e)):
            ans.append(e[i])
            ans.append(o[i])
            
        return ans
        
#url: https://leetcode.com/problems/sort-array-by-parity-ii/
