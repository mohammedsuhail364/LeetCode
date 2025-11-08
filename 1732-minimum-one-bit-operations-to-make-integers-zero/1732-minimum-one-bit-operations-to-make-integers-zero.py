class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        res=0
        while n>0:
            res^=n
            n=n>>1
        return res
    #    n(4) = 100
    #    n>>1 = 010
    #    n>>2 = 001
    #    n>>3 = 000

    #    100 
    #    010 ^
    #    ---
    #    110
    #    001 ^
    #    ---
    #    111 -> 7
    # | n | binary | f(n) -> convert cost  
    # | - | ------ | ---- |
    # | 0 | 000    | 0    |
    # | 1 | 001    | 1    |
    # | 2 | 010    | 3    |
    # | 3 | 011    | 2    |
    # | 4 | 100    | 7    |
    # | 5 | 101    | 6    |
    # | 6 | 110    | 4    |
    # | 7 | 111    | 5    |
    # This pattern is not arbitrary — it is exactly the Gray Code ordering.
    # f(n)=n^(n>>1)^(n>>2)^(n>>3)…
    

