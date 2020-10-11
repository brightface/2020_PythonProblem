import sys
sys.stdin = open("input.txt")


def Count(len):
    cnt = 0
    for x in arr:
        cnt += (x//len)
    return cnt

n,m = map(int, input().split())
arr = [int(input()) for i in range(n)]

res=0
lt = 1
rt = max(arr)
#print(rt)
#지금 현재 숫자로 한다.
while lt <= rt:
    mid = (lt+rt) // 2
    #더 길이가 클수록 정답이다. LT가 최대한 커진다.
    if Count(mid) >= m:
        res = mid
        lt = mid +1
    else:
        rt = mid -1
print(res)
