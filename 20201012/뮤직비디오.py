import sys
#sys.stdin = open("input.txt")

n,m = map(int,input().split())

arr = list(map(int,input().split()))
lt = 1
rt = n
#print(arr)
#최소값을 구하는것이다. 최대값이 아니라. 따라서 거기에 따라 합을 다 구한다음 나눠준다음에 최소값을 구해야해
rt = sum(arr)
res = 0 # 45 이분검색해야지! 2분검색해서 !

def Count(capacity):
    cnt = 1
    sum = 0
    for x in arr:
        if sum + x > capacity:
            cnt += 1 #새로운 디비디가 필요해
            sum = x
        else:
            sum += x
    return cnt

while lt <= rt:
    mid = (lt+rt)//2
    if Count(mid) <= m: #무조건 한곡은 들어가야한다.
        res = mid
        rt = mid -1 #  더 작은수찾아가야지 맞으면
    else: # 더 작은수 찾아가야지x  더 큰수찾아갸야지
        lt = mid +1

print(res)
