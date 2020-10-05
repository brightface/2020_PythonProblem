import sys
#sys.stdin = open("input.txt")


n = int(input())
answer = [0] * (n+1)
for i in range(n):
    #리스트로 안받아도 된다.
    tmp = input().split() #저절로 문자 리스트로 받아진다. split함수
        #따라서 리스트로 받아졋으니까 map으로 쪼갤수 있다.
    tmp.sort(reverse=True)
    a,b,c = map(int,tmp)
    #print(a,b,c)
    if a == b and b == c:
        answer[i] = 10000 + a*1000
    elif (a == b and b != c):
        answer[i] = 1000 + a*100
    elif (a != b and b == c):
        answer[i] = 1000 + b*100
    elif (a == c and b != c):
        answer[i] = 1000 + a* 100
    elif a!= b and b!=c and c!=a:
        answer[i] = a*100

ans = max(answer)
print(ans)