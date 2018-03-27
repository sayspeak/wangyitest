n = int(input())
array = list(map(int,input().split()))
k,d = map(int,input().split())
resArray = [[[0] * 2 for j in range(k+1)] for i in range(n)]
result = 0;
for i in range(0,n):
    resArray[i][1][0],resArray[i][1][1]=array[i],array[i]
    for j in range(2,k+1):
        for m in range(max(i-d,0),i):
            resArray[i][j][0] = max(resArray[i][j][0]
                ,max(resArray[m][j-1][0]*array[i],resArray[m][j-1][1]*array[i]))
            resArray[i][j][1] = min(resArray[i][j][1]
                ,min(resArray[m][j-1][0]*array[i],resArray[m][j-1][1]*array[i]))
    result = max(result,max(resArray[i][k][0],resArray[i][k][0]))
print(result)