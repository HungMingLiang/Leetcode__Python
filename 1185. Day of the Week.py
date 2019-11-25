class Solution(object):
    def isLeap(self,year):
        return ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0 and year % 4000 != 0))
    
    def dayOfTheWeek(self, day, month, year):
        """
        :type day: int
        :type month: int
        :type year: int
        :rtype: str
        """


        wL=[ "Thursday","Friday", "Saturday","Sunday", "Monday", "Tuesday", "Wednesday"]
        mL=[31,28,31,30,31,30,31,31,30,31,30,31]

        daySum=0

        for i in range(1970,year):

            if self.isLeap(i):
                daySum+=366
            else:
                daySum+=365

        if self.isLeap(year):
            mL[1]=29

        for i in range(month-1):
            daySum+=mL[i]

        daySum+=day



        return wL[daySum%7-1]
        
#url:https://leetcode.com/problems/day-of-the-week/
