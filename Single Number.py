class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        for k in range(len(nums)):
            value = nums.pop(0)
            try: 
                nums.remove(value)
            except:
                return value