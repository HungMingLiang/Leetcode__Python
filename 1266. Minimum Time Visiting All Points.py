class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        x,y=points[0][0],points[0][1]
        points.pop(0)
        time=0
        for point in points:
            tupleCompare=(abs(point[0]-x),abs(point[1]-y))
            tMax=max(tupleCompare)
            tMin=min(tupleCompare)
            time=(tMax-tMin)+tMin+time
            x,y=point[0],point[1]

        return time
        
#url:　https://leetcode.com/problems/minimum-time-visiting-all-points/
