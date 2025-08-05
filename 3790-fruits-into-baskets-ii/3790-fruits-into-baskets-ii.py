class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        is_fruits_available=[False]*len(fruits)
        is_baskets_free=[False]*len(baskets)
        for i in range(len(fruits)):
            for j in range(len(baskets)):
                if not is_baskets_free[j] and fruits[i]<=baskets[j]:
                    is_baskets_free[j]=True
                    is_fruits_available[i]=True
                    break
        return is_fruits_available.count(False)