import sys
sys.stdin = open("input.txt")
n = int(input())
arr = list(map(int,input().split()))
maxL = len(arr)-1
answer = []
p = []
lt = 0
rt = len(arr)-1
result = -1
cnt = 0
#print(lt, rt)
#2차원 배열형식으 로 풀면 더 짧음.
if arr[lt] > arr[rt]:
    result = arr[rt]
    p.append(result)
    answer.append('R')
    rt-=1
    cnt += 1
else:
    result = arr[lt]
    p.append(result)
    answer.append('L')
    lt+=1
    cnt += 1

while not lt == rt:
    if lt > maxL or rt < 0:
        break
    if result <arr[lt] and result < arr[rt] :
        if arr[lt] > arr[rt]:
            result = arr[rt]
            p.append(result)
            cnt += 1
            rt -= 1
            answer += 'R'
            #arr.pop()
        else:
            result = arr[lt]
            p.append(result)

            lt += 1
            cnt += 1
            answer.append('L')
    elif result < arr[lt]:
        result = arr[lt]
        answer.append('L')
        p.append(result)
        cnt+=1
        lt+=1
        #rt-=1
    elif result < arr[rt]:
        result = arr[rt]
        answer.append('R')
        p.append(result)
        cnt += 1
        rt -= 1
        #lt += 1
    else :
        break
        #arr.pop(0)
#print(p)
print(cnt)
print(''.join(answer))

