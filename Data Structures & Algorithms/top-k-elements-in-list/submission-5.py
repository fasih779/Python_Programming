class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        re = defaultdict(int)

        for i in nums:
            re[i] += 1

        res = [x[0] for x in sorted(re.items(), key=lambda x: x[1], reverse=True)[:k]]

        return res