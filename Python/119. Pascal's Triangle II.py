# Runtime 26ms | Beats 96.43% of submissions
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0: return [1]
        rows = [[1]*(i+1) for i in range(rowIndex+1)]
        for i in range(2, rowIndex+1):
            for j in range(1, i):
                rows[i][j] = rows[i-1][j-1] + rows[i-1][j]
        return rows[-1]
