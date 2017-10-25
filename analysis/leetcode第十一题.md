leetcode第十一题

Given *n* non-negative integers *a1*, *a2*, ..., *an*, where each represents a point at coordinate (*i*, *ai*). *n* vertical lines are drawn such that the two endpoints of line *i* is at (*i*, *ai*) and (*i*, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and *n* is at least 2.

题意解析：

给定一个list，以list的下标为横坐标，值为纵坐标，组成一个坐标点，向横坐标坐标做垂线，任意找两条线，与很轴围成一个桶求出桶的最大容量，桶不可以倾斜

解题思路：

木桶理论，最薄弱的一面决定桶的容量，因此桶的容量与两条线中较由短的一条决定，其容量也是横坐标做差与纵坐标中较小的一个乘积，假定横坐标差值为矩形的长，纵坐标较小的为宽，那么最大的宽为第一个点与最后一个点，以此为初始条件，向里面收拢，i = 0 ,j = length -1 如果height[i]<height[j],那么向i应该向后面靠拢，因为j向前靠拢对于整个面积只能是减少，反之亦然，靠拢后面积与当前面积比对，取较大的，直至i=j

代码实现：

```python
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        length = len(height)
        maxcon = 0
        container = 0
        i = 0
        j = len(height)-1
        while i< j:
            container = (j-i)*self.getsmall(height[i],height[j])
            if container > maxcon:
                maxcon = container
            if height[j] > height[i]:
                i+=1
            else:
                j-=1
        return maxcon
    def getsmall(self,n1,n2):
        if n1 >= n2:
            return n2
        else:
            return n1
```

