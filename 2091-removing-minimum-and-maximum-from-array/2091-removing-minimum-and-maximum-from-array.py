class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        index={v:i for i,v in enumerate(nums)}
        minVal = min(nums)
        maxVal = max(nums)
        minIndex = min(index[minVal],index[maxVal])
        maxIndex = max(index[minVal],index[maxVal])
        print(minIndex)
        print(maxIndex)
        one = minIndex + 1 + len(nums) - maxIndex
        two = maxIndex +1
        three = len(nums) - minIndex
        return min(one,two,three)