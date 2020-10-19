import sys
from collections import deque
#deque 가져오기 from collections from deque
#sys.stdin = open("input.txt")
n , m = map(int, input().split())
que = [(pos, val) for pos, val in enumerate(list(map(int, input().split())))]
#1차원 리스트 * 1차원 튜플 = 2차원 <= 튜플형태로 받기
#1차원 배열로 접근한다.
cnt=1
#deque선언
que = deque(que)
while True:
    #큐의 pop은 대입이 가능하다.
    cur = que.popleft()
    # if cur[0] == m:
    if any(x[1] > cur[1] for x in que):
        que.append(cur)
    else:
        if cur[0] == m:
            print(cnt)
            break
        else:
            cnt += 1

    #C style
    # for x in que:
    #     if x[1]>cur[1]:
    #         que.append(cur)

    # for pos, val in que:
    #     if
    # print(1)
