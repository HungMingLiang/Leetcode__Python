class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        tL=[x for x in t] #make list of t

        for i in range(len(s)):
            try:
                tL.remove(s[:1]) #try remove first char of s in t list
                s=s[1:] #remove first char in s
            except: #if fail means it is not Anagram
                return False
        
        if tL==[]: #after check all char if t list is empty return True
            return True
        return False
        
#url: https://leetcode.com/problems/valid-anagram/
