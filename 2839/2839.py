N = int(input()) #설탕 N킬로그램
#N은 3이상 5000이하
result=0
while N>=0:
    if N % 5 == 0:
        result+=N // 5
        print(result)
        break
    N-=3
    result+=1
if N < 0:
    print(-1)
    





