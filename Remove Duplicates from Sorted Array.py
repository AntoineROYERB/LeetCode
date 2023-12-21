#https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        my_set = set()
        index = 0
        for i in range(len(nums)):
            if nums[i - index] in my_set:
                nums.pop(i - index)
                index += 1
            else:
                my_set.add(nums[i - index])
        return len(nums)