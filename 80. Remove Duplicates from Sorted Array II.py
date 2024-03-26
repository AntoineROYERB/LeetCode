class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        countDuplicates = {}
        i = 0
        while i < len(nums):
            countDuplicates[nums[i]] = countDuplicates.get(nums[i], 0) + 1
            if countDuplicates[nums[i]] > 2:
                nums.pop(i)
            else:
                i += 1
        
        return len(nums)