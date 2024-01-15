#https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/546/
class Solution:
    def twoSum(self, nums: list[int], target: int) -> List[int]:
        for index1 in range(len(nums)):
            for index2 in range(len(nums)):
                if nums[index1] + nums[index2] == target and index1 != index2:
                    return [index1, index2]