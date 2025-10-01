"""
Zero Striping
For each zero in an m x n matrix, set its entire row and column to zero in place

Create Hash Set for track rows contain zeros, and columns contain zeros
- Add its row index to the row hash set (zero_rows)
- Add its columns index to the column hash set (zero_columns)
"""

matrix = [[1, 0, 2, 1], [1, 2, 3, 1], [9, 2, 4, 0], [2, 2, 4, 2]]

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

from typing import List  # noqa: E402


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

"""
In-place Zero Tracking

1. Use a flag to indicate if the first row initially contains any zero
2. Use a flag to indicate if the first column initially contains any zero
3. Traverse the submatrix, setting zeros in the first row and column to serve
as markers for rows and columns that contain zeros.
4. Apply zeros based on markers: iterate through the submatrix that starts from
the second row and second column. For each cell, check if its corresponding
marker in the first row or column is marked with a zero. If so, set that element
to zero.
5. If the first row was initially marked as containing a zero, set all elements
in the first row to zero.
6. If the first column was initially marked as having a zero, set all elements
in the first columns to zero.

matrix = [
    [1, 3, 3, 0, 5],
    [6, 0, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 0]
]
"""


def zero_striping(matrix: List[List[int]]) -> None:
    if not matrix or not matrix[0]:
        return

    m, n = len(matrix), len(matrix[0])  # m x n

    first_row_has_zero = False
    first_col_has_zero = False

    for c in range(n):
        if matrix[0][c] == 0:
            first_row_has_zero = True
            break

    for r in range(m):
        if matrix[r][0] == 0:
            first_col_has_zero = True
            break

    for r in range(1, m):
        for c in range(1, n):
            if matrix[r][c] == 0:
                matrix[0][c] = 0
                matrix[r][0] = 0

    for r in range(1, m):
        for c in range(1, n):
            if matrix[0][c] == 0 or matrix[r][0] == 0:
                matrix[r][c] = 0

    if first_row_has_zero:
        for c in range(n):
            matrix[0][c] = 0

    if first_col_has_zero:
        for r in range(m):
            matrix[r][0] = 0


matrix = [[1, 2, 3, 4, 5], [6, 0, 6, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 0]]

[[1, 0, 3, 4, 0], [0, 0, 0, 0, 0], [11, 0, 13, 14, 0], [0, 0, 0, 0, 0]]
