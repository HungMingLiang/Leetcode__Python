class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        comL=[i for i in heights]
        comL.sort()

        count=0
        zipped=zip(heights,comL)

        for z in zipped:
            if z[0]!=z[1]:
                count+=1

        return count
        
#url: https://leetcode.com/problems/height-checker/
