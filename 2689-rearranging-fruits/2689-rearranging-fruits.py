class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        """
        Step 1: Check if it’s even possible

        Combine both baskets and check if each fruit count is even.

        Reason: After making baskets equal, each fruit must appear exactly half in each basket.

        If any fruit appears odd times, return -1.

        Step 2: Identify Surplus Fruits

        For each fruit:

        Compute how many should be in each basket = total_count // 2

        If basket1 has more than needed, those are extra fruits to give away → add to surplus1.

        If basket2 has more than needed, those are extra fruits to give away → add to surplus2.

        These surplus lists represent exactly the fruits that need to be swapped.

        Step 3: Minimize Swap Cost

        Sort surplus1 ascending (cheapest to give away from basket1).

        Sort surplus2 descending (largest to give away from basket2).

        Pair the smallest from one basket with the largest from the other for minimal cost swaps.

        Swap cost formula:

        cost = min(direct_swap_cost, 2 * global_min)
        direct_swap_cost = min(fruit_from_basket1, fruit_from_basket2)

        2 * global_min = cost of double-swapping via the cheapest fruit
        
        """
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