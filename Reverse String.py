#https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/879/

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        my_list = s.copy()
        for i in range (len(s)):
            s[i]  = my_list[-(i + 1)]
