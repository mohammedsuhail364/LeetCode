class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        # | Concept                    | Meaning                                        |
        # | -------------------------- | ---------------------------------------------- |
        # | Each element can move `±k` | So the total range can shrink by `2k`          |
        # | If the original gap < 2k   | The intervals overlap → you can make all equal |
        # | If the gap > 2k            | Some difference remains → gap - 2k             |
        return max(0,max(nums)-min(nums)-(2*k))
