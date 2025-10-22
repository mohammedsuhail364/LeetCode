class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        unused=(1<<len(words))-1
        memo={}
        def helper(start_word,unused):
            if unused==0:
                return start_word
            if (start_word,unused) in memo:
                return memo[(start_word,unused)]
            shortest=None
            for i in range(len(words)):
                if unused & (1<<i):
                    super_string=helper(words[i],unused ^ (1<<i))
                    overlap=overlap_append(start_word,super_string)
                    if shortest is None or len(overlap)<len(shortest):
                        shortest=overlap
            memo[(start_word,unused)]=shortest
            return memo[(start_word,unused)]
        def overlap_append(a,b):
            max_overlap=""
            for i in range(1,min(len(a),len(b))+1):
                suffix_of_A = a[-i:]
                prefix_of_B = b[:i]
                if suffix_of_A == prefix_of_B:
                    remain_in_A=a[:-i]
                    remain_in_B=b[i:]
                    max_overlap=remain_in_A+suffix_of_A+remain_in_B
            return max_overlap if max_overlap != "" else a+b
        return helper("",unused)