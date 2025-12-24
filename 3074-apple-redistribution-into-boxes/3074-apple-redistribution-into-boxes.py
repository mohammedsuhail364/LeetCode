class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse=True)
        apples=sum(apple)
        for i in range(len(capacity)):
            apples-=capacity[i]
            if apples<=0:
                return i+1
        