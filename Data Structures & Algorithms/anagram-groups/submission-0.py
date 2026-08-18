class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = {}
        for s in strs:
            k = str(sorted(s))
            if k not in h: h[k] = []
            h[k].append(s)
        return[v for _,v in h.items()]
        