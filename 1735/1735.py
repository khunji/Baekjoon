import math

A = list(map(int,input().split()))
B = list(map(int,input().split()))
C=[None,None]


C[0] = (A[0]*B[1]+B[0]*A[1])
C[1] = (A[1]*B[1])


print(int(C[0]/math.gcd(C[0],C[1])),int(C[1]/math.gcd(C[0],C[1])))



