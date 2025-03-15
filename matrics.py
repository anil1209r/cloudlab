
# Create a 2x2 matrix
matrix = [[1, 2], 
          [3, 4]]

# Print the matrix
print("Matrix:")
for row in matrix:
    print(row)

# Accessing elements
print("\nElement at position (0, 0):", matrix[0][0])
print("Element at position (1, 1):", matrix[1][1])

# Matrix addition (adding the same matrix for simplicity)
matrix2 = [[1, 2], 
           [3, 4]]
result = [[matrix[i][j] + matrix2[i][j] for j in range(2)] for i in range(2)]

print("\nMatrix Addition Result:")
for row in result:
    print(row)

# Matrix multiplication (multiplying the same matrix for simplicity)
result = [[0, 0], [0, 0]]

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        for k in range(len(matrix2)):
            result[i][j] += matrix[i][k] * matrix2[k][j]

print("\nMatrix Multiplication Result:")
for row in result:
    print(row)
