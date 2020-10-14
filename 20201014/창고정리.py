import sys
#sys.stdin = open("input.txt")

n = int(input())
arr = list(map(int,input().split()))
m = int(input())
cnt1=-1
cnt2=-1
for i in range(m):
    tmp1= max(arr)
    tmp2= min(arr)
    for j in range(n):
        if arr[j] == tmp1:
            cnt1 = j
        if arr[j] == tmp2:
            cnt2 = j
    arr[cnt1] -= 1
    arr[cnt2] += 1

print(max(arr)-min(arr))