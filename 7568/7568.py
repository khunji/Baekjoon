N = int(input())

number = []

for i in range(N):
    [w,h] = map(int,input().split())
    number.append([w,h])

for i in number:
    rank=1
    for j in number:
        if i[0] < j[0] and i[1] < j[1]:
            rank+=1
    print(rank, end=' ')
