import sys
sys.stdin= open("input.txt")
n = int(input())
a = [0 for _ in range(n+1)]
flag = [0 for _ in range(n+1)]
def solution():
    if n == 2:
        answer= 1
        return answer
    elif n == 3:
        answer = 2
        return answer
    else:
        tmp = int(n / 2)
        for i in range(2, tmp ):  # 1~n/2까지 돌면서 그 다음 숫자나오면 2 면 ~n/2까지 돌고 곱해지는수로 반복
            for j in range(i, n + 1, i):
                if a[j] == 0:
                    if flag[j] == 0:
                        flag[j] = 1
                    else :
                        a[j] = 1
    return n-sum(a)
print(solution())








