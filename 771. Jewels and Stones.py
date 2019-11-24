class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count=0
        for j in J:
            count+=S.count(j) #count j occurrence
        
        return count

#url: https://leetcode.com/problems/jewels-and-stones/
