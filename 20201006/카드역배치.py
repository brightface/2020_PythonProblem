import sys
#sys.stdin = open("input.txt")

arr = [i for i in range(1,21)]

for i in range(10):
    a, b = map(int,input().split())
    tmp = arr[a-1:b]

    tmp = tmp[::-1]
    arr[a-1:b] = tmp
#리스트에 join이 있는게 아니라 문자열에 있네, list는 append있네;;
#map은 list로 반환해줘야한다.
#arr = (arr)
#arr = int(arr)
arr= list(map(str,arr))
print(' '.join(arr))