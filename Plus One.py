#https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/559/
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        res = ''
        digits_plusOne = []
        for digit in digits:
            res += str(digit)

        res = str(int(res) + 1)
        for digit in res:
            digits_plusOne.append(int(digit))
        return digits_plusOne