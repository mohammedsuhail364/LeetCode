class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        freq=Counter(basket1)+Counter(basket2)
        for fruit,count in freq.items():
            if count%2:
                return -1
        freq1=Counter(basket1)
        freq2=Counter(basket2)
        surplus1=[]
        surplus2=[]
        for fruit,total in freq.items():
            needed_each=total//2
            if freq1[fruit]>needed_each:
                surplus1.extend([fruit]*(freq1[fruit]-needed_each))
            if freq2[fruit]>needed_each:
                surplus2.extend([fruit]*(freq2[fruit]-needed_each))
        res=0
        global_min=min(min(basket1),min(basket2))
        surplus1.sort()
        surplus2.sort(reverse=True)
        for i,j in zip(surplus1,surplus2):
            res+=min(min(i,j),2*global_min)
        return res