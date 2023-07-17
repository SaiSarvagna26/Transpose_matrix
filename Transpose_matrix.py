def get_transpose_of_matrix(matrix, m, n):
    transpose=[]
    for i in range(n):
        row=[]
        for j in range(m):
            row.append(matrix[j][i])
        transpose.append(row)
    return transpose    

m, n = input().split()
m, n = int(m), int(n)
num_list = []

for i in range(m):
    list_a = list(map(int,input().split()))
    num_list.append(list_a)

transpose=get_transpose_of_matrix(num_list, m, n)
for row in transpose:
    print(row)
