class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        """
        intuation :-
        ------------
        \U0001f9e9 Step 1: Understand What the differences Array Means
        Let’s say you don’t know the actual hidden sequence, but you do know:

        hidden[1] - hidden[0] = 1 → So hidden[1] = hidden[0] + 1

        hidden[2] - hidden[1] = -3 → So hidden[2] = hidden[1] - 3 = hidden[0] + 1 - 3

        hidden[3] - hidden[2] = 4 → So hidden[3] = ...

        So the entire hidden sequence depends on the first value, hidden[0].
        
        \U0001f9e9 Step 2: Build the Hidden Sequence from hidden[0]
        Let’s assume:

        hidden[0] = x
        Then we calculate the next values:

        text
        Copy
        Edit
        hidden[1] = x + 1
        hidden[2] = x + 1 - 3 = x - 2
        hidden[3] = x - 2 + 4 = x + 2
        So the sequence becomes:

        python
        Copy
        Edit
        [x, x+1, x-2, x+2]
        Now, we want all values of this sequence to be between 1 and 6.

        So:

        text
        Copy
        Edit
        x must be in a range where:
        x ≥ 1               (so the first number is ≥ 1)
        x+1 ≤ 6             (so second number ≤ 6)
        x-2 ≥ 1             (so third number ≥ 1)
        x+2 ≤ 6             (so last number ≤ 6)

        This gives:
        x ≥ 1
        x ≤ 5
        x ≥ 3   → from x - 2 ≥ 1
        x ≤ 4   → from x + 2 ≤ 6

        So all combined:
        x must be between 3 and 4 → only 2 values
        ✅ There are only 2 valid values for hidden[0] that make the entire sequence lie in [1, 6].
        """
        prefix_sum=[0]*(len(differences)+1)
        for i in range(1,len(differences)+1):
            prefix_sum[i]=prefix_sum[i-1]+differences[i-1]
        min_prefix=min(prefix_sum)
        max_prefix=max(prefix_sum)
        min_x=lower-min_prefix
        max_x=upper-max_prefix
        res=max(0,max_x-min_x+1)
        return res