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

        count = sorted(count, key=lambda num: count[num], reverse=True)
        
        return count[:k]
