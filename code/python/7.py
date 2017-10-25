class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > 2147483648 or x <-2147483648:
            return 0
        tag = 0
        temp = []
        if x < 0:
            x = -x
            tag = 1
        temp = list(str(x))
        temp.reverse()
        temp = "".join(temp)
        temp = int(temp)
        if tag == 1:
            temp = -1*temp
        if  temp > 2147483648 or temp <-2147483648:
            return 0
        else:
            return temp

if __name__ == '__main__':
    s = Solution()
    print(s.reverse(1534236469))



