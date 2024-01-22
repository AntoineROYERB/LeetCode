#https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/770/
class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # We first transpose the given matrix, and then reverse the content of individual rows to get the resultant 
        # 90 degree clockwise rotated matrix.
        N = len(matrix)

        # Transpose the matrix
        for i in range(N):
            for j in range(i+1,N):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

        # Reverse individual rows
        for i in range(N):
            for j in range(N//2):
                matrix[i][j],matrix[i][-(j +1)] = matrix[i][-(j +1)],matrix[i][j]