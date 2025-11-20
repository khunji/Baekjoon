def solution(n,a,b):
    newA = sorted(A) #오름차순
    newB = sorted(B,reverse=True)#내림차순
    S=0

    for i in range(n):
        S+=newA[i]*newB[i]
    return S

N = int(input()) #N
A = list(map(int,input().split())) #A배열
B = list(map(int,input().split())) #B배열

result = solution(N,A,B)

print(result)