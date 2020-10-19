import sys
sys.stdin = open ("input.txt")

arr = list(map(str,input()))
pt =[]
k = []
answer = []
flag = 0
res = ""
#연산자 우선순위가 잘 모르겠다. * / 가 연산자 우선순위가 높고 + - 가 연산자 우선순위가 낮다. ( ) 연산자 우선순위가 높다.
#닫는괄호 만났으면 여는괄호 나올떄까지 연산자 무조건 처리해야한다.
def MakePostfix(arr):
    for i in arr:
        if i.decimal():
            res += i
        else:
            if i == '(':
                flag =1
            k.append(i)


print(arr)