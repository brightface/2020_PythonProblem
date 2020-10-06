import sys
#sys.stdin = open("input.txt")

n1 = int(input())
arr1 = list(map(int,input().split()))
n2 = int(input())
arr2 = list(map(int,input().split()))
arr1.sort()
#print(arr1)
arr2.sort()
#print(arr2)
a = 0
b = 0
answer = []

while (a< n1 and b<n2):
    if arr1[a] < arr2[b]:
        answer.append(arr1[a])
        a+=1
    elif arr1[a] > arr2[b]:
        answer.append(arr2[b])
        b+=1
    else:
        answer.append(arr1[a])
        answer.append(arr2[b])
        a+=1
        b+=1
if(a>=n1):
    #list append와
    # + 의 차이

    answer+=arr2[b::]
else:
    answer+=arr1[a::]
print(' '.join(list(map(str,answer))))
