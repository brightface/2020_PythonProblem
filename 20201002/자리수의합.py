import sys
#sys.stdin= open("input.txt")

def digit_sum(x):
    tmp=0
    while(x>0):
        tmp += x % 10
        x //= 10
    return tmp

num = int(input())
arr = list(map(int,input().split()))
mx = -2147000000


maxIdx = -2
for i,j in enumerate(arr):
    #rint(digit_sum(j))
    if mx < digit_sum(j):
        mx = digit_sum(j)
        maxIdx = i
print(arr[maxIdx])



