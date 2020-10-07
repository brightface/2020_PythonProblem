import sys
#sys.stdin = open("input.txt")

st=0
end=1
n,answer=map(int,input().split())
arr = list(map(int,input().split()))
cnt=0
#print(n,answer,arr)
tot=arr[0] #투포인터 시작 잡는것도 중요해 sum으로 푸는거 아니야

# tot = sum(arr[st:end])
while 1: #while st<n or end<n : 이게 안된다. 아래서 쪼개야돼
    if tot > answer :
        tot -= arr[st]
        st += 1

    elif tot == answer:
        tot -= arr[st]
        st += 1
        cnt += 1

    else:
        if end<n: #여기서 쪼개야한다.
            tot += arr[end]
            end +=1
        else: break
#논리가 한변에 펼져지지 않는다. while문!! 그 안에서 쪼개야 하는 two 포인터 알고리즘이다!

#print(answer)
print(cnt)

#ar=[3,2,1] #sum은 뒤로 안더해진다.
#print(sum(ar[1:3]))
# 1. 스트레스 받아서 공부 안되어있을때 운동하면 공부 되긴하지 더 잘되긴 하지
# 2. 근데 중요한건 서울대의 의지력이야. 집중력보다 의지력이 중요할때가 있다.
# 집중의 의지력.을 기르자. 권다정 윗입술이 아랫입술 깨무는 너를 보며 꺠우칠떄가 있다.
# 단 환경이 조금 갖춰져야 이런 집중의 의지력이 나올수 있다. 아니면 1번 알고리즘 따라간다.
#2번이 중요해 진짜!!
