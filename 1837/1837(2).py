P,K = map(int,input().split())


def is_prime(n):
    if n < 2:
        return False
    for j in range(2,int(n**0.5)+1):
        if n%j==0:
            return False
    return True


for i in range(2,K):    #2부터 K-1까지만 검사
    if is_prime(i) and P % i == 0:
        print("BAD",i)
        break
else:
    print("GOOD")