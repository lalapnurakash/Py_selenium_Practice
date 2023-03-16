def ConvertBinary(n):
    if n>1:
        ConvertBinary(n//2)
    print(n%2,end="")
print("the binary of the given number is")
ConvertBinary(8)

A=[[1,2,3],
   [2,4,1],
   [5,6,2]]
B=[[2,6,7],
   [4,3,2],
   [2,5,1]]
result=[[0,0,0],
   [0,0,0],
   [0,0,0]]
for i in range (len(A)):
    for j in range(len(A[0])):
        result[i][j]=A[i][j]+B[i][j]

