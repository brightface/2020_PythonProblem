import sys
#
# #sys.stdin=open("input.txt")
# cardCnt,cnt = map(int,input().split())
# arr = list(map(int,input().split()))
# sum=0
# answer =[]
# for i in range(cardCnt):
#     for x in range(i+1,cardCnt):
#         for j in range(x+1, cardCnt):
#             sum = arr[i]+arr[x]+arr[j]
#             answer.append(sum)
#             sum=0
# #set은 add로 더한다.
# answer.sort(reverse=True)
# #print(answer)
# set(answer)
# list(answer)
# print(answer)
# print(answer[cnt-1])
#10 3
#13 15 34 23 45 65 33 11 26 42

sys.stdin=open("input.txt")
cardCnt,cnt = map(int,input().split())
arr = list(map(int,input().split()))

answer=set()
for i in range(cardCnt):
    for x in range(i+1,cardCnt):
        for j in range(x+1, cardCnt):
            #answer.append(sum)
            answer.add(arr[i]+arr[x]+arr[j])

answer = list(answer)
answer.sort(reverse=True)
print(answer[cnt-1])
#set은 add로 더한다.
#print(answer)
# set(answer)
#형변환 할때는 또 넣네. 함수로 할때는 안넣으면서

