class Solution(object):
    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        
        ans=[]
        j=True
        length=len(A)

        while j:
            maxInd=0
            maxVal=A[0]
            for i in range(length):
                if A[i]>maxVal:
                    maxInd=i
                    maxVal=A[i]
            A[0:maxInd+1]=A[0:maxInd+1][::-1]
            A[0:length]=A[0:length][::-1]
            ans.append(maxInd+1)
            ans.append(length)
            length-=1
            print(A)
            temp=A[0]
            for n in range(1,len(A)):
                if temp<A[n]:
                    temp=A[n]
                else:
                    break
            else:
                j=False
            
        
        return ans

#url:https://leetcode.com/problems/pancake-sorting/https://leetcode.com/problems/pancake-sorting/
