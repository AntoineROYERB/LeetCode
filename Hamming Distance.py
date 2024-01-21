#https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/762/
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        hammingDistance = 0
        max_len = max(len(bin(x)), len(bin(y)))

        x_bin = bin(x)[2:].zfill(max_len)
        y_bin = bin(y)[2:].zfill(max_len)

        for index in range(max_len):
            if x_bin[index] != y_bin[index]:
                hammingDistance += 1

        return hammingDistance
sol = Solution()
sol.hammingDistance(4,14)