import sys
#sys.stdin = open("input.txt")

n, r = map(int,input().split())
arr = [i for i in range(1,n+1)]

#
# arr.pop(2)
# print(arr)
# arr.pop(4)
# print(arr)
# arr.pop(5)
# print(arr)
index = r-1
#print(arr[index])
arr.pop(index)
#print(arr)

while arr:
    if len(arr) == 1:
        break
    # if index != 0:
    index -= 1
    for i in range(r):
        index += 1
        if index >= len(arr):
            index = 0
    #print(arr[index])
    arr.pop(index)
    #print(arr)
print(arr[0])