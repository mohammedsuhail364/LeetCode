class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        res=set()
        prev=set()
        for i in arr:
            cur={i | j for j in prev}
            cur.add(i)
            res.update(cur)
            prev=cur
        return len(res)