class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        ss=s.strip().split()
        ss.reverse()
        sL=(i for i in ss)

        return ' '.join(sL)

#url:https://leetcode.com/problems/reverse-words-in-a-string/
