class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        print(freq)
        return [num for num, count in freq.most_common(k)]
        