import math

class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num<0 or num==0:
            return False
        return math.log(num, 4).is_integer()
        
#url: https://leetcode.com/problems/power-of-four/
