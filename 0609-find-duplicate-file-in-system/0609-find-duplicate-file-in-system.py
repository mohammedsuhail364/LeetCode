class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_map=defaultdict(list)

        for path in paths:
            path=path.split()
            root=path[0]
            for p in path[1:]:
                num,text=p.split('.')
                w=root+'/'+num+'.'+text[:3]
                content_map[text].append(w)
        return [files for files in content_map.values() if len(files)>1]