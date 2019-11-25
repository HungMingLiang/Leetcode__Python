class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        A=[a*a for a in A]
        A.sort()
        return A
       
#url: https://leetcode.com/problems/squares-of-a-sorted-array/
