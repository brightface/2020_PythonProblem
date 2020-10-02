import sys

#10
#45 73 66 87 92 67 75 79 75 80
#sys.stdin=open("input.txt")

cnt = int(input())
a = list(map(int,input().split()))
sum = 0
for i in range(cnt):
    sum+=a[i]
avg = round(sum/cnt)

min = 9999999999
temp = 999999999
for x in range(cnt):
    if abs(avg-a[x]) < min:
        min = abs(avg - a[x])
        answer = x + 1
        temp = a[x]
    elif abs(avg-a[x]) == min:
        if(a[x] == temp):
            continue
        else:
            if(a[x]-avg > 0):
                min = abs(a[x]-avg)
                answer = x + 1
                temp = a[x]
            else:
                continue
print(avg , answer)
