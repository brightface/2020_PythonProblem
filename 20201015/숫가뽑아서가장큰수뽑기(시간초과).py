import sys
#sys.stdin = open ("input.txt")

a,b = map(int,input().split())
#print(a)

cnt = b
max_tmp= 0
flag =0
a = list(str(a))
# print(a)
a = list(map(int,a))
# print(a)
#파이썬은 이게 힘드네 씨언어는 그냥 앞에 자료형 적어주면 되는데
while cnt>0 :
    flag=0
    for i,k in enumerate(a): #와 이게 되네 파이썬은, 동적배열 크기 줄어들때마다 그 숫자에 맞춰서 하기.
        if flag ==1 :
            break
        for j in range( i-1 ,-1, -1):
            if a[i]>a[j]:
                if cnt>0:
                    # a.pop(0)
                    p=a[0:j+1]
                    # print(p)
                    tmp=(min(p))
                    a.pop(a.index(tmp))
                    cnt-=1
                    flag=1

a = list(map(str, a))
a=''.join(a)
print(a)


