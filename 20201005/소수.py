import sys
#sys.stdin= open("input.txt")
n = int(input())

def solution():
    a = [0 for _ in range(n + 1)]
    flag = [0 for _ in range(n + 1)]
    # print(a)
    # print(flag)
    if n == 1:
        answer = 0
    elif n == 2:
        answer= 1
        return answer
    elif n == 3:
        answer = 2
        return answer

    else:
        tmp = int(n / 2)
        a[1]=1

        for i in range(2, tmp+1):  # 1~n/2까지 돌면서 그 다음 숫자나오면 2 면 ~n/2까지 돌고 곱해지는수로 반복
            flag[i]=1
            for j in range(i, n + 1, i):
                if a[j] == 0:
                    if flag[j] == 0:
                        a[j] = 1

                        #print(a)

            flag[i]=0

    return n-sum(a)

print(solution())








