#암호 P와 K가 주어진다.
#암호 P는 특정한 소수 p와 q의 곱으로 이루어진 수
#만약 p와 q 중 하나라도 K보다 작은 암호는 좋지 않은 암호-->BAD와 p와 q중 작은 소수 출력
#만약 p와 q 모두 K보다 큰 수이면 좋은 암호-->GOOD 출력



P,K = map(int,input().split())
#P와 K를 입력받음

#입력된 P까지의 소수를 판단
#판단한 소수 중에서 P의 약수가 있는지 판단

d=[]    #판단한 소수를 이 리스트에 넣어준다.


for i in range(2, P): #2부터 P까지 소수를 찾는다
    is_prime=True
    for j in range(2,int(i**0.5)+1):    #2부터 루트 i까지만
        if i%j==0:
            is_Prime=False
            break
    if is_prime:
        d.append(i)

    
#d에는 P까지의 소수가 저장되있음.
#여기서 P가 어떤 소수로 나누어 떨여지는지 확인하고 더 작은 것을 출력할지 정함
r=0
stat=0

for i in d:
    if P%i==0:
        r=min(i,(P//i))
        if i<K and (P//i)<K:
            stat='BAD'
        else:
            stat="GOOD"
    
    else:
        pass

if stat=='BAD':
    print(stat,r)
else:
    print(stat)






