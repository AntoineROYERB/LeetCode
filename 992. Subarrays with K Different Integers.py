class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        ans, n, left, cnt = 0, len(nums), 0, 0
        for right in range(n + 1):
            unique_int = len(set(nums[left:(right)]))
            print(nums[left:right], unique_int)
            if  unique_int == k: cnt += 1
            while unique_int !< k:
                left += 1   
                unique_int = len(set(nums[left:right]))
            ans += cnt      
        return ans    
