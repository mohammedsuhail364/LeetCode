class Solution:
    def calPoints(self, operations: List[str]) -> int:
        li=[]
        for i in operations:
            if i=='C':
                li.remove(li[-1])
            elif i=='D':
                li.append(li[-1]*2)
            elif i=='+':
                li.append(li[-1]+li[-2])
            else:
                li.append(int(i))
        return sum(li)