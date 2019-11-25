class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        
        if num==0:
            return False
        num=float(num)
        while True:
            n2=num/2
            n3=num/3
            n5=num/5
            if n2.is_integer():
                
                num=n2
            elif n3.is_integer():
                
                num=n3
            elif n5.is_integer():
                
                num=n5       
            else:
                break

        return num==1
        
#url: https://leetcode.com/problems/ugly-number/
