def find_neighbourhood(matrix, m, n, x, y):
    neighbourhood = []
    if (x + 1) <= (m - 1):
        neighbourhood.append(matrix[x + 1][y])
    if (x - 1) >= 0:
        neighbourhood.append(matrix[x - 1][y])
    if (y + 1) <= (n - 1):
        neighbourhood.append(matrix[x][y + 1])
    if (y - 1) >= 0:
        neighbourhood.append(matrix[x][y - 1])
    return neighbourhood


row = int(input())
column = int(input())
user_matrix = [[int(j) for j in input().split()] for i in range(row)]
x_user = int(input())
y_user = int(input())

neighbourhoods = sorted(find_neighbourhood(
                            user_matrix,
                            row,
                            column,
                            x_user,
                            y_user))
if len(neighbourhoods) > 0:
    print(' '.join(str(x) for x in neighbourhoods))
