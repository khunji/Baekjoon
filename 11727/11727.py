#문제 2*n 직사각형을 1*2, 2*1과 2*2타일로 채우는 방법의 수를 구하는 프로그램을 작성해라.

#입력
#첫째 줄에 n이 주어진다. 

#출력
#첫째 줄에 2*n 크기의 직사각형을 채우는 방법의 수를 10007로 나눈 나머지를 출력한다.

import sys
input = sys.stdin.readline

def square(arr,a):
    if a==1:
        return 1
    if a==2:
        return 3
    
    arr[1]=1
    arr[2]=3
    for i in range(3,a+1):
        arr[i] = (arr[i-1] + arr[i-2] + arr[i-2])
    return arr[a]%10007

n = int(input())#첫째 줄에 n이 주어진다.

dp = [0]*(n+1)

print(square(dp,n))



