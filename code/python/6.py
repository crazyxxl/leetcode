class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        listres = []
        length  = len(s)
        if numRows == 1:
            return s
        if length < numRows:
            return s
        else:
            i = 0
            tag = 0
            trend = 0
            while i<numRows:
                listres.append([s[i]])
                i+=1
                tag+=1
            while tag<=numRows and tag>=-1 and i < length:
                if tag == -1:
                    tag = 1
                    trend = 1
                if tag == numRows:
                    tag = numRows-2
                    trend = 0
                listres[tag].append(s[i])
                if trend == 0:
                    tag-=1
                if trend == 1:
                    tag +=1
                i+=1
            res = ""
            for item in listres:
                temp = "".join(item)
                res = res+temp
            return res