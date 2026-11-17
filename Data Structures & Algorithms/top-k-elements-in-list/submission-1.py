class Solution:
    def upsert(self, num, dict):
        if num in dict:
            dict[num] += 1
        else:
            dict[num] = 1

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            self.upsert(num, count)

        count = heapq.nlargest(
            k,
            count,
            key=lambda num: count[num]
        )

        return count
