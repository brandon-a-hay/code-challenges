matrix = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]

def get_diag_sum(matrix):
    sum = 0
    for i in range(len(matrix)):
        sum += matrix[i][i]

    return sum
    

diag1_sum = get_diag_sum(matrix)
diag2_sum = get_diag_sum(matrix)
print(abs(diag1_sum - diag2_sum))

