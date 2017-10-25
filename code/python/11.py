class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        length = len(height)
        area_max = 0
        container = 0
        i = 0
        j = len(height)-1
        while i< j:
            container = (j-i)*self.getsmall(height[i],height[j])
            if container > area_max:
                area_max = container
            if height[j] > height[i]:
                i+=1
            else:
                j+=1
        return area_max
    def getsmall(self,n1,n2):
        if n1 >= n2:
            return n2
        else:
            return n1

