class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        ans=[]
        sumA=sum([a for a in A if a%2==0])

        for q in queries:
            temp= A[q[1]]+q[0]

            if temp%2==0:
                if A[q[1]]%2==0:
                    sumA=sumA+(temp-A[q[1]])
                else:
                    sumA=sumA+temp

            else:
                if A[q[1]]%2==0:
                    sumA=sumA-(A[q[1]])
            ans.append(sumA)

            A[q[1]]=temp


        return ans
        
#url: https://leetcode.com/problems/sum-of-even-numbers-after-queries/
