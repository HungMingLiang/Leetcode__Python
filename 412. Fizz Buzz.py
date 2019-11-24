class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        s=[]
        for i in range(1,n+1):
            if i % 15 ==0:
                s.append('FizzBuzz')
            elif i%3==0:
                s.append('Fizz')
            elif i%5==0:
                s.append('Buzz')
            else:
                s.append(str(i))
        return s
        
#url: https://leetcode.com/problems/fizz-buzz/
