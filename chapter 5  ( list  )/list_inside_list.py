
matrix=[[1,2,3],[4,5,6],[7,8,9]]
# 3 items---->3 lists

print(matrix[1])      # to print individual list in list

for i in matrix :     # to print lists in list
    print(i)

for sublist in matrix :    # print all elemnet in lists
    for i in sublist :
        print(i)

print(matrix[1][2])       # to print individual element of list

# type method  //// define data type of list

print(type(matrix))
