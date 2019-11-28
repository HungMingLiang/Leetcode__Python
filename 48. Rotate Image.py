class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        a=zip(*matrix[::-1])

        for aa in a:
            matrix.pop(0)
            matrix.append(list(aa))
            
#url: https://leetcode.com/problems/rotate-image/
