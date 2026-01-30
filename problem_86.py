# Problem 86: Find sum of matrix diagonals
# Fixed version

def diagonal_sum(matrix):
    n = len(matrix)
    total = 0

    for i in range(n):
        total += matrix[i][i]          # main diagonal
        if i != n - 1 - i:             # avoid double count
            total += matrix[i][n-1-i]  # secondary diagonal

    return total

mat = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

print(f"Diagonal sum: {diagonal_sum(mat)}")

