def fun(matrix):
    n = len(matrix)
    m = len(matrix[0])
    ans = True
    for i in range(1,n):
        for j in range(1,m):
            if matrix[i][j]!=matrix[i-1][j-1]:
                ans = False
                break
        if ans==False:
            break
    return ans
matrix = [[1,3,3],[4,1,2],[3,4,1]]
val = fun(matrix)
if(val):
    print("Valid Matrix")
else:
    print("Invalid Matrix")