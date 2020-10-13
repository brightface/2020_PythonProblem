import sys
#아예 안되면 rt 감소 맞네
#되면 lt 증가시키고
#sys.stdin = open("input.txt")

n,c = map(int, input().split())
arr = []
for i in range(n):
    arr.append(int(input()))
#print(arr)
arr.sort()
rt = arr[n-1]
lt=1
#문제가 잘못되었나? 아니다. 니가 잘못 알아들은거야. 억지성으로 알아들음 문제를 풀기위한 문제로(힘들어서? ㅋㅋ 안힘들어 잘알아들으면) - 아니다 이것또한 개소리
#문제를 잘 풀었다. 문제를 풀기위한 문제도 푸는거야. 실수가 있었어 단순한 반복문 어디까지돌리나의 실수 아니네. 잘못푼거 맞네
# 으악 시발
def Count(mid):
    cnt = 1
    st=arr[0]
    for i in range(1,n): #여기가 잘못되었는데?
        if arr[i]-st >= mid: #여기가 잘못되었엇네 mid 보다 클떄 는 넣을수 있으니 참이다.
            cnt += 1
            st = arr[i]
    return cnt
res =0
while lt <= rt:
    mid = (lt+rt)//2
    if Count(mid) >= c:
        res = mid
        lt=mid +1

    else :
        rt=mid -1

print(res)
