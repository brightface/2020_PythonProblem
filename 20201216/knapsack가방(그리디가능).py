import sys
sys.stdin = open("input.txt")

n , max_weight = map(int,input().split())
# print(n,max_weight)
info = [list(map(int,input().split())) for i in range(n)]

#j까지 담을수 있는 최대 가치
dy=[0]*(max_weight+1)
#print(dy)

#top down 방식 인가 bottom up 이나 top down 인것 같 ㄴㄴ bottom up
#0부터 채운다.
#2중포문으로 돌려야 하나?
#빼야하는데
for i in range(n):
    for j in range(info[i][0],max_weight+1):
        #if i-w >= 0:
            dy[j] = max(dy[j-info[i][0]]+info[i][1],dy[j])
        #else:
         #   break
print(dy)
print(max(dy))