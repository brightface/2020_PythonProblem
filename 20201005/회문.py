import sys
sys.stdin = open("input.txt")

n = int(input())

for i in range(n):
    chr = input()
    chr = chr.upper() #대입안해주면 안된다. 형변환과 마찬가지/
    if(chr == chr[::-1]):
        print("#%d YES" %(i+1))
    else:
        print("#%d NO" %(i+1))


