#1,2로 자를수 있을때 네트워크 선이 주어졌으때 자르는 방법의 경우의수는?
import sys
sys.stdin = open("input.txt")


def DFS(n): #n은 네트워크 선이고 dfs는 자를수 있는 경우의 수이다. (자를때 순서도 다르면 다른걸로 친다.)
    # if  n>= 2 :
    #     return 1
    # if n == 1 and n == 2  :
    #     return
    if arr[n] > 0 : return arr[n] #이게 메모리 제이션 #동적계획법 #다이나믹 프로그래밍 #트리 계산전에 계산했던걸 이용해서 바로 리턴
    #########################
    elif n == 1: return 1
    elif n == 2 : return 2
    else :
        arr[n]= DFS(n-1)+DFS(n-2)
        return arr[n]

if __name__ == "__main__":
    n = int(input())
    arr = [0] * (n + 1)
    arr[1]=1
    arr[2]=2

    print(DFS(n))

   # print(arr[n])

