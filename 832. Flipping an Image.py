class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        ansA=[]

        for a in A:
            a.reverse() #reverse a
            temp=[1 if i==0 else 0 for i in a] #1 to 0, 0 to 1
            ansA.append(temp)
        
        return ansA
        
#url: https://leetcode.com/problems/flipping-an-image/
