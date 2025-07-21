class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        idx=defaultdict(list)
        for i in range(len(groupSizes)):
            idx[groupSizes[i]].append(i)
        # print(idx)
        res=[]
        for x,y in idx.items():
            while y:
                temp=[]
                for i in range(x):
                    temp.append(y.pop())
                res.append(temp)
        return res