class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        res=[]
        for h in range(12):
            h_count=bin(h).count('1')
            for m in range(60):
                m_count=bin(m).count('1')
                if h_count+m_count==turnedOn:
                    res.append(f"{h}:{m:02d}")
        return res
                
