class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        ans = 0
        mp = {}
        left = 0
        n = len(nums)
        for right in range(n):
            mp[nums[right]] = mp.get(nums[right], 0) + 1
            if mp[nums[right]] > k:
                while nums[left] != nums[right]:
                    mp[nums[left]] -= 1
                    left += 1
                mp[nums[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans