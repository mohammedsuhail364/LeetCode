class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        n=len(words)
        unused=(1<<n)-1
        @lru_cache(None)
        def helper(start_word,unused):
            if unused==0:
                return start_word
            shortest=None
            for i in range(n):
                if unused & (1<<i):
                    super_string=helper(words[i],unused^(1<<i))
                    overlap=overlap_append(start_word,super_string)
                    if shortest is None or len(overlap)<len(shortest):
                        shortest=overlap
            return shortest
        def overlap_append(a,b):
            max_overlap=""
            for i in range(1,min(len(a),len(b))+1):
                suffix_of_A=a[-i:]
                prefix_of_B=b[:i]
                if suffix_of_A==prefix_of_B:
                    remain_in_A=a[:-i]
                    remain_in_B=b[i:]
                    max_overlap=remain_in_A+suffix_of_A+remain_in_B
            return max_overlap if max_overlap!="" else a+b 

        return helper("",unused)
