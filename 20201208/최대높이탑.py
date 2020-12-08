import sys
#sys.stdin = open("input.txt")
n = int(input())
brick = []

#하나씩 끊어서 변수 대입받아서 어펜드하기
for i in range(n):
    #arr.(tuple(map(int,input().split())))
    width, height, weight = map(int,input().split())
    brick.append([width, height, weight])

#brick.sort(reverse=True)
brick.sort(key = lambda x:x[0], reverse = True)

dy=[0]*(n)
#dy는 탑에 n번째의 벽돌을 놓았을때의 최대 높이
#초기화 먼저

for i in range(n):
    if i == 0:
        dy[i]=brick[i][1]
    else:
        maxT = 0 #최대 높이
        for j in range(i):
            # max = brick[j][2]
            # 무게가 더 작을때
            if brick[j][2] > brick[i][2]:
                #최대 높이라면
                if maxT < dy[j]:
                    maxT = dy[j]
        dy[i] = maxT + brick[i][1]
            # else :
            #     maxT = 0
        #다이마님 들어가서 이제 이전상황 생각안해 #높이 더한다.
        #print(brick[i][2])

#print(dy)
print(max(dy))
#print(brick)
