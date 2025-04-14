"""

Problem Explanation:

Given a string, divide it into partitions where:

characters at each partition DOES NOT appear in any other partition
then return the length of each one.
Good Luck!

Sol-
Try to greedily choose the smallest partition that includes the first letter. 
If you have something like "abaccbdeffed", then you might need to add b.
You can use an map like "last['b'] = 5" to help you expand the width of your partition.

"""

class Solution:
    def partitionLabels(self, s: str):
        di={s1:i for i,s1 in enumerate(s)}   
        i=0
        res=[]
        while i<len(s):
            last=di[s[i]]
            x=i
            while x<len(s) and x<=last:
                if di[s[x]]>last:
                    last=di[s[x]]
                x+=1
            res.append(last-i+1)
            i=last+1
        return res