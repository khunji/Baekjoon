def solution(vps):
    balance=0

    for ch in vps:
        if ch == '(':
            balance+=1
        else:
            balance-=1

        if balance < 0:
            return "NO"
    
    if balance == 0:
        return "YES"
    else:
        return "NO"
        

        

N = int(input()) # 테스트 케이스


for _ in range(N):
    arr = input().strip()
    print(solution(arr))
    