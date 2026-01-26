from typing import List
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        idx={n:i for i,n in enumerate(order)}
        l=0
        for r in range(1,len(words)):
            first,second=words[l],words[r]
            for i in range(len(first)):
                if i==len(second): # eg: apple > app 
                    return False 
                if idx[first[i]]>idx[second[i]]:
                    return False
                elif idx[first[i]]<idx[second[i]]:
                    break
            l+=1
        return True