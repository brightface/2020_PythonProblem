import sys
#sys.stdin = open("input.txt")

n = int(input())
arr = list(map(int,input().split()))
max_money = int(input())

dy = [110]*(max_money+1)
#print(dy)
dy[0]=0 #0으로 해야 한다. 그래야 된다. 초기화 이게 중요하다. 오답 나오는 이유
#다이나믹의 초기화 중요

#이건필요없다.
# dy[1]=1
# dy[2]=1
# dy[5]=1
#print(arr)
# 다이 나믹 프로그래밍으로 풀었다. bottom up 방식
for i in range(1, n+1):
    for j in range(arr[i-1], max_money+1):
        #print(j) # i - 1 하는것에서 시간 엄청 끌었다. 정수 조심해라.
        #print("end")
       dy[j] = min(dy[j - arr[i-1]] + 1 , dy[j])
# print(dy)
print(dy[max_money])
# print(n,arr,max_money)