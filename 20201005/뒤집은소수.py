import sys
#sys.stdin = open("input.txt")

n = input()
a = list(map(str, input().split()))

def IsPrime(n):

    arr = [0]*(n+1)
    if n == 1 : return True
    for i in range(2,n) :
        if arr[i] == 0:
            for j in range(i,n+1,i):
                arr[j]=1

    if arr[n] == 1:
        return True
    else:
        return False

for i in a:
    i = i[::-1]
    i=int(i)

    if IsPrime(i) == False:
        print(i, end=' ')

