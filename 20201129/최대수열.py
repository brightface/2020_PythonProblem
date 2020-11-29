import sys
sys.stdin = open("input.txt")
n = int(input())

inArr = list(map(int,input().split()))
#print(inputArr)


# def Dfs(n) : #n은 배열의 인덱스
#     flag =0
#     for i in range(0,n) :
#         tmp = -1
#         mx = -1
#
#         for j in range(0, i):
#             if inputArr[i] > inputArr[j]:
#                 for k in range(0,i):
#                     flag=0
#                     if tmp <= ans[k] and flag == 0:
#                         tmp = ans[k]
#                         mx = tmp
#                         flag =1
#                     elif tmp <= ans[k] and flag == 1:
#                         tmp = ans[k]
#                         if tmp > mx :
#                             mx = tmp
#                             ans[i] = mx+1
#                             tmp=ans[i]

def king(n):
    for i in range(0,n):
        tmp = -1
        for j in range(0,i):
            if inArr[i]>inArr[j] :
                if tmp<=ans[j]:
                    ans[i] = ans[j] +1 #메모리제이션
                    tmp = ans[i]


if __name__ == "__main__":
    ans = [1] * (n + 1)
    king(n)
    print(max(ans))


