import sys
#sys.stdin = open("input.txt")
n = int(input())
arr = [list(map(int,input().split())) for i in range(n)]
dy = [[0]*(n) for i in range(n)]
dy[0][0] = arr[0][0]
for i in range(n):
    dy[0][i] = dy[0][i-1]+arr[0][i]
    dy[i][0] = dy[i-1][0]+arr[i][0]
for i in range(1,n):
    for j in range(1,n):
        dy[i][j] = min(dy[i-1][j], dy[i][j-1]) + arr[i][j]
#dfs,bfs로 안하고 동적프로그래밍으로도 할수 있구나.

#print(dy)
print(dy[n-1][n-1])