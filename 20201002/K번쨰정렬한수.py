import sys
sys.stdin = open("input.txt")

testCases = int(input())

# ▣ 입력예제 1
# 2
# 6 2 5 3
# 5 2 7 3 8 9
# 15 3 10 3
# 4 15 8 16 6 6 17 3 10 11 18 7 14 7 15
# ▣ 출력예제 1
#1 7
#2 6

for i in range(testCases):
    # for i in range(numCnt):
    #     arr[i]=
    numCnt, start, end, cnt = map(int, input().split())
    arr = list(map(int, input().split()))
    arr = arr[start-1:end]
    arr.sort()
    print("#%d"%(i+1), end=" ")
    print(arr[cnt-1])


