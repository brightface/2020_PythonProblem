import sys
sys.stdin = open("input.txt")

n = int(input())
meeting = []
for i in range(n):
    a ,b = map(int ,input().split())
    meeting.append((a,b))

meeting.sort(key = lambda x : (x[1],x[0]) )
#sort 와 key // 그리고 람다함수
#C++에도 sort 함수에 람다함수 해주는거 있어

# while 1:
et = 0
cnt = 0
#회의 빠르게 끝나는 시간으로 정렬한다. 먼저 끝나는것부터 세기 위해서. <그리디>
for s, e in meeting:
    if s >= et: #그리고 시작보다 끝이 크면..되는걸로
        et = e
        cnt+=1

print(cnt)



#print(meeting)
