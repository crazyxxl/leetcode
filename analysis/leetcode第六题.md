leetcode第六题：

The string `"PAYPALISHIRING"` is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

```
P   A   H   N
A P L S I I G
Y   I   R
```

And then read line by line: 

```
"PAHNAPLSIIGYIR"
```

Write the code that will take a string and make this conversion given a number of rows:

```
string convert(string text, int nRows);
```

```
convert("PAYPALISHIRING", 3)
```

 should return 

```
"PAHNAPLSIIGYIR"
```

题意解析：

将一个字符串排成锯齿形然后按行输出：

例子：

````
nRows = 3
P   A   H   N
A P L S I I G
Y   I   R
output：PAHNAPLSIIGYIR
nRow = 4

P    I    N
A  L S  I G
Y A  H R
P    I
output:PINALSIGYAHRPI
````

![6](/home/xxl/文档/学习总结文档/leetcode/imgs/6.png)

代码实现：

```python
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
if __name__ == '__main__':
    s = Solution()
    print(s.convert("ABC",1))
```

