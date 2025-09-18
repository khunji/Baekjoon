N,M = map(int,input().split())

castle=[]

for i in range(N):
     castle.append(input())
        
countrow=0
countcol=0

for i in range(N):
    if 'X' not in castle[i]:
        countrow += 1

for j in range(M):
    found = False
    for i in range(N):
        if 'X' in castle[i][j]:
            found=True
            break
    if not found:
        countcol+=1

print(max(countrow,countcol))