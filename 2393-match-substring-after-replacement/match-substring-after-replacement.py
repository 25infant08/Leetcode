class Solution:
    def matchReplacement(self, s: str, sub: str, mappings: List[List[str]]) -> bool:
        s_maps = defaultdict(lambda : set())
        for x,y in mappings:
            s_maps[x].add(y)
        subs = [s_maps[c] | {c} for c in sub] 
        for i in range(len(s)-len(sub) + 1):
            c=s[i]            
            j=i
            while j-i<len(sub) and s[j] in subs[j-i]:                                        
                j+=1
            if j-i==len(sub): 
                return True
        return False   