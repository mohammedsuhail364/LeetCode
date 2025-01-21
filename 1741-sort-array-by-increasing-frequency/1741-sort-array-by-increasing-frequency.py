class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        li=[]
        k=Counter(nums)
        res=defaultdict(list)
        for i,j in k.items():
            if j not in res:
                res[j].append(i)
            else:
                res[j].append(i)
        for val in res.values():
            val.sort(reverse=True)
        
        sortedDict=dict(sorted(res.items()))
        
        for i,j in sortedDict.items():
            for x in j:
                li+=[x]*i
        return li