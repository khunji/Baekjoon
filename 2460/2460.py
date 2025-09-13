people=[]
cnt=0
for i in range(10):
    
    o,i = map(int, input().split())#out의 o, in의 i 직관적으로 변수 설정
    cnt=cnt+i-o
    people.append(cnt)

print(max(people))
