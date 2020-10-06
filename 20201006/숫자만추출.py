import sys
sys.stdin = open("input.txt")

n = input()
a=[]
b=[]
#len 함수 , decimal함수 - 리스트일때만 된다. 문자열을 리스트로.
for i in range(len(n)):
    a.append(n[i])
    if a[i].isdecimal():
        b.append(a[i])

answer=''.join(b)
answer= int(answer)
print(answer)
cnt=0
for i in range(1,answer+1):
    if answer%i ==0:
        cnt += 1
print(cnt)


