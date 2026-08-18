class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        for n in nums:
            if n in hm: hm[n] +=1
            else: hm[n] = 1
        kx=list(hm.values())
        kx.sort(reverse=True)
        l =[]
        for i in hm:
            if hm[i] in kx[:k]:
                l.append(i)
        return l