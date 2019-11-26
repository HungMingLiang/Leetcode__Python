class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        length=len(arr)
        ind=0

        while ind<length:
            if arr[ind]==0:
                arr.insert(ind,0)
                ind+=2
                arr.pop()
            else:
                ind+=1


#url: https://leetcode.com/problems/duplicate-zeros/
