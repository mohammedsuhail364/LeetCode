class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def convert_to_star(word):
            res=''
            for i in word:
                if i in 'aeiou':
                    res+='*'
                else:
                    res+=i
            return res
        exact=set(wordlist)
        case_map={}
        vowel_error_map={}
        for word in wordlist:
            x=word.lower()
            devowel=convert_to_star(x)
            if x not in case_map:
                case_map[x]=word
            if devowel not in vowel_error_map:
                vowel_error_map[devowel]=word
        res=[]
        for q in queries:
            if q in exact:
                res.append(q)
            else:
                lower=q.lower()
                devowel=convert_to_star(lower)
                if lower in case_map:
                    res.append(case_map[lower])
                elif devowel in vowel_error_map:
                    res.append(vowel_error_map[devowel])
                else:
                    res.append('')
        return res