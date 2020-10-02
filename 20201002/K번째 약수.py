import sys
sys.stdin = open("input.txt")

#▣ 입력예제 1
#6 3
#▣ 출력예제 1
#3

n, k = map(int, input().split())
cnt = 0
#1부터 n+1까지
for i in range(1 , n+1):
    if n%1 == 0:
        cnt=cnt+1
    if cnt == k :
        print(i)
        break
#python 은 for else 구문이 있다. break를 만나면 else를 하지 않는데 정상적으로 끝나면 else를 한다.
else:
    print(-1)


