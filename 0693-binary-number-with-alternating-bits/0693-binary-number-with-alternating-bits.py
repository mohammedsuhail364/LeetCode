class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        
        # Step 1: Right shift n by 1
        # Example:
        # n = 21
        # binary:        10101
        # right_shift -> 01010
        right_shift = (n >> 1)
        
        # Step 2: XOR original number with shifted version
        # If bits are alternating, every adjacent bit differs,
        # so XOR will produce all 1s.
        #
        #   10101
        # ^ 01010
        # --------
        #   11111
        temp = n ^ right_shift
        
        # Step 3: Check if temp is of form 11111 (all 1s)
        #
        # Property:
        # If temp = 11111
        # Then temp + 1 = 100000
        #
        #    11111
        # & 100000
        # --------
        #    000000
        #
        # So (temp & (temp + 1)) == 0
        # means temp was all 1s → original number had alternating bits
        return (temp & (temp + 1)) == 0
