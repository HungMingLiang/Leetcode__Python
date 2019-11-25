class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        times=len(s)
        count=0
        sL=[]
        for i in range(times):
            if len(s)==0:
                break
            if count%2==0:
                sL.append(s[:k][::-1])
            else:
                sL.append(s[:k])
            count+=1
            s=s[k:]


        return ''.join(sL)
        
#url: https://leetcode.com/problems/reverse-string-ii/
