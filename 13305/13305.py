import sys

def solution(dis, ol):

    current_ol_price = dis[0] * ol[0] #첫 번째 도시에서 두 번째 도시를 갈 때는 어쩔 수 없이 첫 번째 도시의 기름을 무조건 넣어야 한다.
    current_ol = ol[0]  #다음 도시와의 기름 가격을 비교하기 위한 변수이다. 일단 첫 번째 도시의 기름 가격을 넣어둔다.

    new_dis = dis[1:]
    new_ol = ol[1:-1]
    
    for i,j in zip(new_ol,new_dis):
        if current_ol > i:
            current_ol = i
            current_ol_price += current_ol * j
        else:
            current_ol_price += current_ol * j
    
    return current_ol_price
        


N = int(sys.stdin.readline())#도시의 개수

distance = list(map(int,sys.stdin.readline().split()))#도시 간의 거리를 입력한다.

oil = list(map(int,sys.stdin.readline().split()))#도시에서 1L의 가격을 입력한다.

print(solution(distance, oil))



