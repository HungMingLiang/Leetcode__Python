class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        sL = s.split(' ')
        ans = ''
        for ss in sL:
            ss = ss[::-1]
            ans =ans+' '+ss
        ans=ans.strip()

        return ans

#url: https://leetcode.com/problems/reverse-words-in-a-string-iii/
