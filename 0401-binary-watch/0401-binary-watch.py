class Solution:
    def readBinaryWatch(self, n: int) -> List[str]:
        res=[]
        for h in range(12):
            for m in range(60):
                h_ones=bin(h).count('1')
                m_ones=bin(m).count('1')
                if h_ones+m_ones==n:
                    res.append(f"{h}:{m:02d}")
        return res
