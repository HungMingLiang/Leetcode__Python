class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a=int(a,2)
        b=int(b,2)
        ans=bin(a+b)
        return ans[2:]
        
#url: https://leetcode.com/problems/add-binary/
