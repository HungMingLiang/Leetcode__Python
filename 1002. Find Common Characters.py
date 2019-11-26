class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        S=[[i for i in a] for a in A]
        ans=[]
        length=len(A)-1
        for i in range(len(S[0])):
            count=0
            for j in range(1,len(S)):

                if S[0][i] in S[j]:
                    S[j].remove(S[0][i])
                    count+=1
                    if count==length:
                        ans.append(S[0][i])
                else:
                    break
        
        return ans

#url: https://leetcode.com/problems/find-common-characters/
