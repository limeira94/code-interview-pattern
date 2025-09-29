"""
Zero Striping
For each zero in an m x n matrix, set its entire row and column to zero in place

Create Hash Set for track rows contain zeros, and columns contain zeros
- Add its row index to the row hash set (zero_rows)
- Add its columns index to the column hash set (zero_columns)
"""

matrix = [
    [1, 0, 2, 1],
    [1, 2, 3, 1],
    [9, 2, 4, 0],
    [2, 2, 4, 2]
]

zero_rows = {0, 2}
zero_columns = {1, 3}

matrix[0][0] == 0
matrix[0][1] == 0
matrix[0][2] == 0
matrix[0][3] == 0

matrix[0][1] == 0
matrix[1][1] == 0
matrix[2][1] == 0
matrix[3][1] == 0

matrix[2][0] == 0
matrix[2][1] == 0
matrix[2][2] == 0
matrix[2][3] == 0

matrix[0][3] == 0
matrix[1][3] == 0
matrix[2][3] == 0
matrix[3][3] == 0

from typing import List # noqa: E402


def zero_striping_hash_sets(matrix: List[List[int]]) -> None:

    m, n = len(matrix), len(matrix[0])
    
    zero_rows = set()
    zero_columns = set()
    
    for r in range(m):
        for c in range(n):
            if matrix[r][c] == 0:
                zero_rows.add(r)
                zero_columns.add(c)
    
    for r in range(m):
        for c in range(n):
            if r in zero_rows:
                matrix[r][c] = 0
            if c in zero_columns:
                matrix[r][c] = 0

"""
Time complexity --> O(m*n)
Space complexity --> O(m+n)
"""