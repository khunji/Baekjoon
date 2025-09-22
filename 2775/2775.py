T=int(input()) #테스트 케이스

for i in range(T):
    k=int(input())
    n=int(input())

    floor_zero = [f for f in range(1,n+1)] #0층의 사는 사람들을 저장
    #floor_zero = [1,2,3...n]

    for j in range(1,k+1): #1,2, ... k k층만큼 반복하기
        for y in range(1,n): #floor_zero의 인덱스
            floor_zero[y]+=floor_zero[y-1]
        print(floor_zero[-1])


    

