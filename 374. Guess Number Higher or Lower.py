# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if guess(n)==0:
            return n
        if guess(1)==0:
            return 1

        max=n
        min=1
        g=int((max+min)/2)
        
        while True:
            if guess(g)==1:
                min=g
                g=int((max+min)/2)
            elif guess(g)==-1:
                max=g
                g=int((max+min)/2)
            else:
                break
        
        return g
        
#url: https://leetcode.com/problems/guess-number-higher-or-lower/
