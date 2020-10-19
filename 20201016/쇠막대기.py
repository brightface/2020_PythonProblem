import sys
sys.stdin = open("input.txt")

#괄호 나오면 스택에 넣는다
inputArr = list(input())
# print(inputArr)
stack = []
n = len(inputArr)
ans = 0


# ()(((()())(())()))(())
# 스텍은 input 뒤에서 부터 처리해야한다.
count = 0
for i in range(n-1,-1,-1):
    if inputArr[i] == ')':
        stack.append(inputArr[i])
    #
    # else:
    #     stack.pop()
        #ans += len(stack)
        #if inputArr[i+1] == ')':
        #     ans += len(stack)
        # else: #막대기가 끝나는 경우
        #     ans += len(stack)

        # for i in range(n - 1, -1, -1):
        #     if inputArr[i] == ')':
        #         stack.append(inputArr[i])
        #
    else:
        stack.pop()
        if inputArr[i + 1] == ')':
            ans += len(stack)
        else:  # 막대기가 끝나는 경우
            ans += 1
        #else:

print(ans)

#ㄴㄷ ㅈ ㅅ ㄱ ㅎㄲ ㄹ ㄱ ㄴ ㄹ ㅋ ㅎ ㄱ ㅅ ㄷ

