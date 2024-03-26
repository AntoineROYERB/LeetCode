class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        num_set = set(nums)
        max_list = max(num_set)
        
        for i in range(1, max_list + 2):
            if i not in num_set:
                return i
        return 1