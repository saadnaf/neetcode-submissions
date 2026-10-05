class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        spiral = []
        rows = len(matrix)
        cols = len(matrix[0])
        size = rows * cols
        startRow = 0
        startCol = 0

        while len(spiral) < size:
            self.traverseRight(spiral, matrix, rows, cols, startRow, startCol)
            startRow += 1
            self.traverseDown(spiral, matrix, rows, cols, startRow, startCol)
            cols -= 1
            if startRow < rows:
                self.traverseLeft(spiral, matrix, rows, cols, startRow, startCol)
                rows -= 1
            if startCol < cols:
                self.traverseUp(spiral, matrix, rows, cols, startRow, startCol)
                startCol += 1

        return spiral

    def traverseRight(self, spiral, matrix, r, c, sr, sc):
        for i in range(sc, c):
            spiral.append(matrix[sr][i])

    def traverseDown(self, spiral, matrix, r, c, sr, sc):
        for i in range(sr, r):
            spiral.append(matrix[i][c-1])

    def traverseLeft(self, spiral, matrix, r, c, sr, sc):
        for i in range(c-1, sc-1, -1):
            spiral.append(matrix[r-1][i])

    def traverseUp(self, spiral, matrix, r, c, sr, sc):
        for i in range(r-1, sr-1, -1):
            spiral.append(matrix[i][sc])