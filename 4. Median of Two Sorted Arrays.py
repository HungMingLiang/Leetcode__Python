class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        for num in nums2:
            nums1.append(num)
        nums1.sort()
        length=len(nums1)
        di2=int(length/2)
        if length%2==0:
            return (float(nums1[di2])+float(nums1[di2-1]))/2
        else:
            return nums1[di2]
        
#url: https://leetcode.com/problems/median-of-two-sorted-arrays/
