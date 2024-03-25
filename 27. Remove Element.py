class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        counter = 0
        for index in range(len(nums)):
            if nums[index] == val:
                nums[index] = "_"
                counter += 1
        for index in range(counter):
            nums.remove("_")
        return len(nums)
