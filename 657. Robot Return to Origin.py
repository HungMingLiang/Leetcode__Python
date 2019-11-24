class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        return moves.count('R')==moves.count('L') and moves.count('U')==moves.count('D') #check R count = L count and U count = D count

#url: https://leetcode.com/problems/robot-return-to-origin/
