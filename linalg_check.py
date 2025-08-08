from tantheta.linear_algebra import (
    compute_determinant,
    compute_inverse,
    compute_rank,
    compute_eigenvalues,
    compute_eigenvectors,
    compute_transpose,
    compute_trace,
    matrix_multiplication,
    is_symmetric,
    solve_linear_system,
)

# Sample matrices
matrix1 = [[2, 3], [1, 4]]
matrix2 = [[1, 0], [0, 1]]
coeff_matrix = [[2, 1], [1, -1]]
constants = [3, 1]

print("Determinant:", compute_determinant(matrix1))
print("Inverse:", compute_inverse(matrix1))
print("Rank:", compute_rank(matrix1))
print("Eigenvalues:", compute_eigenvalues(matrix1))
print("Eigenvectors:", compute_eigenvectors(matrix1))
print("Transpose:", compute_transpose(matrix1))
print("Trace:", compute_trace(matrix1))
print("Matrix Multiplication:", matrix_multiplication(matrix1, matrix2))
print("Is Symmetric:", is_symmetric(matrix2))
print("Solve Linear System:", solve_linear_system(coeff_matrix, constants))
