import sys
sys.stdin = open("input.txt")

n,c = map(int,input().split())
arr =[]
for i in range(n):
    tmp = int(input())
    arr.append(tmp)
arr.sort()
print(arr)
# arr= arr.sort()
# print(arr) //None이 되버린다. 함수로만 써야 안사라져
sb = [] #// 배열처럼 대입이 안돼 시발
for a in range(n-1):
    # sub = arr[a+1]-arr[a] 배열처럼 대입이 안돼 시발
    sb.append(arr[a+1] - arr[a])
sb.sort(reverse=True)
check = [0]*(n-1)

key = min(sb)
mx = max(sb)
print(sb)
print(mx)

def Count(mid):
    return mid//c

lt=1
rt = max(arr)
res=0
while lt <= rt:
    mid = (lt+rt)/2
    if Count(mid) > key:
        rt-=1 #아예 아닌쪽. 아닌쪽은 rt를 감소시킨다.
    else:
        #mid <=key
        #더 큰쪽으로 가야한다. lt를 증가시켜서 크게 보낸다.
        lt+=1
        res = mid




