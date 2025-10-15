class Solution:
    def numPermsDISequence(self, s: str) -> int:
        # refer this https://www.youtube.com/watch?v=cjFzL8b4bME
        MOD=10**9+7
        N=len(s)
        @cache
        def get_count(index,last):
            if index==N:
                return 1
            left=N-index # this refers how many numbers we want to the complete this sequence
            total=0
            if s[index]=='D':
                for i in range(last): #last refers how many small numbers we have for this number
                    total+=get_count(index+1,i)
                    total%=MOD
            else:
                for i in range(last,left):
                    total+=get_count(index+1,i)
                    total%=MOD
            return total
        total=0
        for i in range(N+1):
            total+=get_count(0,i)
            total%=MOD
        return total