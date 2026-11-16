class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx_dict = {}

        for i in range(len(nums)):
            target_dif = target - nums[i]

            if target_dif in idx_dict:
                return sorted([i, idx_dict[target_dif]])

            if nums[i] not in idx_dict:
                idx_dict[nums[i]] = i