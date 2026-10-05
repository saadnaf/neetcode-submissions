class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        i = 0
        while i != len(matrix):
            j=i+1
            while j != len(matrix):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                j+=1
            i+=1

        for row in matrix:
            row = row.reverse()