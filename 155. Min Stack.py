class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.listN=[]
  

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.listN.append(x)



    def pop(self):
        """
        :rtype: None
        """
        self.listN.pop()


    def top(self):
        """
        :rtype: int
        """
       
        return self.listN[len(self.listN)-1]

    def getMin(self):
        """
        :rtype: int
        """
        min=self.listN[0]
        
        for i in self.listN:
            if i<min:
                min=i
        
        return min
