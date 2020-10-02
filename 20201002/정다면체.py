import sys
#sys.stdin = open("input.txt")

#4 6
arr = [0 for i in range(110)]
n,m = map(int,input().split())
for i in range(1,n+1):
    for j in range(1,m+1):
        arr[i+j] = arr[i+j]+1
temp = max(arr)

for x,y in enumerate(arr):
    if y == temp:
        print(x, end=" ")