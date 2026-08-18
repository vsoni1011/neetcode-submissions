class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t): return False
        h = {}
        for i in range(len(s)):
            if h.get(s[i]): h[s[i]]+=1
            else: h[s[i]]=1
            if h.get(t[i]): h[t[i]]-=1
            else: h[t[i]]=-1
        for k,v in h.items():
            if v!=0: return False
        return True
