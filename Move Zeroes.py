#https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/567/
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        len_nums = len(nums)
        zero_counter = 0
        for num in nums:
            if num == 0: zero_counter += 1

        nums[:len_nums] = [num for num in nums if num != 0]
        nums[len_nums:] = [0] * zero_counter
        return nums