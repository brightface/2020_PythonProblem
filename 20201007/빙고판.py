import sys

#sys.stdin = open("input.txt")
# a, b = map(int, input(), split())
a = int(input())
arr = [list(map(int, input().split())) for i in range(a)] #맵끝날때 ) 이게 한번 더 붙는다.

#출력하기
# for i in a
    # print(i)

Max = -1
su = 0
for i in range(a):
    #print(su)
    su = 0
    for j in range(a):
        su += arr[i][j]
    if Max < su:
        Max = su

for i in range(a):
    #print(su)
    su = 0
    for j in range(a):
        su += arr[j][i]
    if Max < su:
        Max = su

su = 0
for i in range(a):

    su += arr[i][i]
if Max < su:
    Max = su
#print(su)
su = 0
for i in range(a):
    su += arr[i][a - i-1]
if Max < su:
    Max = su
#print(su)
print(Max)