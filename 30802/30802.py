#문제
#티셔츠 한 장과 펜 한 자루가 포함된 웹컴 키트 나눠주기
#티셔츠 : S,M,L,XL,XXL,XXXL (6가지) --> 같은 사이즈의 T장 묶음으로만 주문 가능
#펜 : 한 종류로, P자루씩 묶음으로 주문하거나 한 자루씩 주문할 수 있다.

#참가자 : N명 중 S:S명, M:M명 , L:L명, XL:XL명, XXL:XXL명, XXXL:XXXL명
#티셔츠는 부족하면 절대 안됨. 신청한 사이즈대로 나눠줘야 한다.
#펜은 정확히 참가자 수만큼 준비되어야 한다-->N자루 

#티셔츠를 T장씩 최소 몇 묶음 주문해야 하나?
#펜을 P자루씩 최대 몇 묶음 주문할 수 있고, 그 때 펜을 한 자루씩 몇 개 주문하는지 구하자.

import sys
input = sys.stdin.readline

N = int(input())#참가자의 수

size = list(map(int,input().split()))#티셔츠 사이즈별 신청자의 수

T,P = map(int,input().split())
countT=0
for i in size:

    if i%T==0:
        if i==0:
            pass
        countT+=(i//T)
    else:
        countT+=(i//T)+1

print(countT)
print(N//P,N%P)