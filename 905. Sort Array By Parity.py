class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        count=0 #current index
        for i in range(len(A)):
            if A[count]%2==1: 
                A.append(A.pop(count)) #if odd move to back
            else:
                count+=1 #if number is event move to next element
        return A

#url: https://leetcode.com/problems/sort-array-by-parity/
