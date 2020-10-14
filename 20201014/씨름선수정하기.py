#키가 나보다 한놈이라도 큰놈이 있으면
#그중에서(그 키큰놈들보다) 내가 몸무게가 제일 많이 나가면 된다.
import sys
sys.stdin = open("input.txt")

n = int(input())
arr = []
for i in range(n):
    a,b = map(int,input().split())
    arr.append((a,b))

#arr.sort(key = lambda x : (x[1], x[0]) )
arr.sort(key = lambda x : (x[0], x[1]), reverse=True)
et = arr[0][1]
#print(et)
#print(arr)
st=0
weight_largest=0
cnt =0
tmp_cnt=0
for s, e in arr:
    # tmp_cnt+=1
    # if s <= st:
    #     for i in range(tmp_cnt):
    #         if e >= et:
    #             cnt+=1
    #             et = e
    #             break
    # else:
    #     cnt += 1
    #     st = s
    if e > weight_largest:
        weight_largest = e
        cnt+=1
print(cnt)