#준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.
#동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다.
#이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.

#첫째 줄에 N과 K가 주어진다.
#둘째 줄부터 N개의 줄에 동전의 가치(A)가 오름차순으로 주어진다.

#첫째 줄에 K원을 만드는데 필요한 동전 개수의 최솟값을 출력한다.

import sys



def solution(a,k):

    #동전의 가치가 K원보다 클 경우에는 그냥 무시하면 된다.
    count=0


    for i in a:
        if i>k:
            pass
        else:
            num = k // i
            count+=num

            #남은 돈
            k%=i
    return count
            
        

N,K = map(int,sys.stdin.readline().split())

arr=[]

for _ in range(N):
    arr.append(int(sys.stdin.readline()))

arr.sort(reverse = True) # 내림차순으로 정리(원본 자체를 바꿈.)

print(solution(arr,K))


