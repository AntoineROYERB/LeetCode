class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        firstPart = nums[:k+1]
        del nums[:k+1]
        nums.extend(firstPart)
            

l = [-1,-100,3,99]
k = 2

l = [1,2,3,4,5,6,7]
k = 3

l = [1,2,3]
k = 2
sol = Solution()
sol.rotate(l,k)