class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        count=0
        for i in grid:
            i.reverse()
            for j in i:
                if j<0:
                    count=count+1
                else:
                    break
                    
        
        return count
            
            
#url:https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/
