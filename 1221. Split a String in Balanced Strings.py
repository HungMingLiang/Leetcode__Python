class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        count=0
        temp=0

        for ss in s:
            if ss=='R':
                temp+=1
                s=s[1:]
                
            else:
                temp-=1
                s=s[1:]
                

            if temp==0:
                count+=1

        return count
        
#url: https://leetcode.com/problems/split-a-string-in-balanced-strings/
