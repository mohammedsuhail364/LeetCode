class Solution:
    def removeSubfolders(self, folder) :
        seen=set()
        folder.sort()
        for i in folder:
            is_sub=False
            tmp=i.split('/')
            sub_folder=''
            for x in tmp:
                if x=='':
                    continue
                new_word='/'+x
                sub_folder+=new_word
                if sub_folder in seen:
                    is_sub=True
            if not is_sub:
                seen.add(i)
        return list(seen)