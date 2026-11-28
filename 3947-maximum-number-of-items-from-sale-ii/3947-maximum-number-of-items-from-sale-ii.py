class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        # refer the tech dose
        n=len(items)
        items_with_factor=[0]*(n+1)
        for f,p in items:
            items_with_factor[f]+=1
        items_with_multiplies=[0]*(n+1)
        for i in range(1,n+1):
            for mul in range(i,n+1,i):
                items_with_multiplies[i]+=items_with_factor[mul]
        mini = min(p for _,p in items)
        discount_items=0
        for f,p in sorted(items,key=lambda x:x[1]):
            if p>=2*mini:break # why we break means after this we bought the mini item which gives more item compare to the after this 
            freebies = items_with_multiplies[f] - 1 # remove the itself count which is not the freebie one
            units_to_buy = min(freebies,budget//p)
            discount_items += units_to_buy # which tells how many originals we need to buy at the end we get *2 of copies with the original
            budget-=(units_to_buy*p)
        return 2*discount_items + budget//mini