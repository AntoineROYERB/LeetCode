#https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/565/
class Solution:
    def hammingWeight(self, n: int) -> int:
        s = str(n)
        res = 0
        for bit in s:
            if bit == "1": res += 1
        return res
