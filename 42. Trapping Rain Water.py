# 2 POINTER

# A basic idea comes into peoples mind if two walls are there and we want want to fill water within that wall we just have 
# to fill the water till min of two wall right if it exceeds the value ,it will overflow.

# So, we can set 2 pointers left_max,right_max and check which side is greater,
# if one side is greater iterate on other side because at the min side the water will be filled at its limit. 
# And iterate till pointer is lower than the other one.


class Solution:
    def trap(self, height: List[int]) -> int:
        max_left, max_right, water, i, j = height[0], height[-1], 0, 0, len(height) - 1
        while i<j:
            if max_left <= max_right:
                water += max_left - height[i]
                i += 1
                max_left = max(max_left, height[i])
            else:
                water += max_right - height[j]
                j -= 1
                max_right = max(max_right, height[j])
        return water