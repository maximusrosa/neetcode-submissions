class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_count = {}

        for num in nums:
            if num in nums_count:
                return True
            else:
                nums_count[num] = 1
        
        return False