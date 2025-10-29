class Solution:
    def smallestNumber(self, n: int) -> int:
        bit=bin(n)[2:]
        total=len(bit)
        res='1'*total
        return int(res,2)