class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        length=2**n-1
        """
        why length is 2**n-1 ?
        S1 = "0"

        Sn = S(n-1) + "1" + reverse(invert(S(n-1)))
        Sn = Left + Mid + Right
        len(Sn) = len(S(n-1)) + 1 + len(S(n-1))
        len(Sn) = 2 * len(S(n-1)) + 1
        ---
        # Step 2: Compute First Few Lengths

        Start small.
        2^1 - 1 = 1
        2^2 - 1 = 3
        2^3 - 1 = 7
        2^4 - 1 = 15
        """
        def dfs(length,k):
            if length==1:
                return "0"
            half=length//2
            # 15 -> 7
            if k<=half:
                return dfs(half,k)
            elif k>half+1:
                res=dfs(half,1+length-k)
                """
                1  2  3  4  5  6  7 | 8 | 9 10 11 12 13 14 15
                L  L  L  L  L  L  L   M   R  R  R  R  R  R  R
                Left part = positions 1 → 7
                Right part = positions 9 → 15
                k = 12
                Right part positions:
                9   10  11  12  13  14  15   
                Left part positions:
                1   2   3   4   5   6   7    
                9  ↔ 7
                10 ↔ 6
                11 ↔ 5
                12 ↔ 4
                13 ↔ 3
                14 ↔ 2
                15 ↔ 1
                12 maps to 4
                Use Formula
                Length = 15
                k = 12
                Compute:
                mirrored = length - k + 1
                        = 15 - 12 + 1
                        = 4         
                """
                return '0' if res=='1' else '1'
            else:
                return '1'

        return dfs(length,k)