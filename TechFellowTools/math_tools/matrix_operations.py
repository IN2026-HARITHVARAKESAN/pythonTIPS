
def matrix_addition(matrix_a, matrix_b):
    """Add two matrices."""
    if len(matrix_a) != len(matrix_b):
        print("Matrices must have the same dimensions")
    for row in range(len(matrix_a)):
        if len(matrix_a[row]) != len(matrix_b[row]):
            print("Matrices must have the same dimensions")
        for col in range(len(matrix_a[row])):
            matrix_a[row][col]+=matrix_b[row][col]
    return matrix_a

def matrix_subtraction(matrix_a, matrix_b):
    """Subtract two matrices."""
    if len(matrix_a)!= len(matrix_b):
        print("Matrices must have the same dimensions")
    for row in range(len(matrix_a)):
        if len(matrix_a[row]) != len(matrix_b[row]):
            print("Matrices must have the same dimensions")
        for col in range(len(matrix_a[row])):
            matrix_a[row][col]-=matrix_b[row][col]
    return matrix_a

def matrix_multiplication(matrix_a, matrix_b):
    """Multiply two matrices."""
    if len(matrix_a[0])!= len(matrix_b):
        print("Number of columns in the first matrix must be equal to the number of rows in the second matrix")
    result=[]
    for i in range(len(matrix_a)):
        row=[]
        for j in range(len(matrix_b[0])):
            sum=0
            for k in range(len(matrix_b)):
                sum+=matrix_a[i][k]*matrix_b[k][j]
            row.append(sum)
        result.append(row)
    return result

def matrix_transpose(matrix):
    """Convert rows into columns."""
    new_matrix=[]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if len(new_matrix)<=j:
                new_matrix.append([])
            new_matrix[j].append(matrix[i][j])
    return new_matrix

def matrix_determinant(matrix):
    """Calculate the determinant using recursive expansion."""
    determinant=0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            sub_matrix=[]
            for k in range(len(matrix)):
                if k!=i:
                    sub_matrix.append([matrix[k][l] for l in range(len(matrix[k])) if l!=j])
            determinant+=((-1)**(i+j))*matrix[i][j]*matrix_determinant(sub_matrix)