import sys
#sys.stdin = open("input.txt")

a,b= map(int,input().split())

a= list(map(int,str(a)))
# print(a)
stack=[]

for x in a:
    while stack and b>0 and stack[-1] <x: #스텍은 마지막만 검사
        stack.pop()
        b-=1
    stack.append(x) #스택은 마지막만 검사
#다 된것에서 더 잘라야 할떄! 뒤쪽에서 부터 자른다.
if b != 0:
    stack= stack[:-b] #-b 이게 되게 신기하다. -b+1 , -b+2 되니까


print(''.join(map(str,stack)))


