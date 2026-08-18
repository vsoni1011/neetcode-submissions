class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = Counter(nums)
        result = []
        for num, count in frequency.most_common(k):
            result.append(num)
        return result  