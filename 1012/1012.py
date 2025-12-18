#문제
#한나-->유기농 배추 재비
#해충 방지에 배추흰나비 지렁이가 좋음.-->배추 근처에 서식하며 해충을 잡아 먹음으로써 배추 호보
#어떤 배추에 배추흰나비가 한 마리라도 살고 있으면 이 지렁이는 인접한 다른 배추로 이동할 수 있다.
#그 배추들 역시 해충으로부터 보호받을 수 있다. 한 배추의 상하좌우 네 방향에 다른 배추가 위치한 경우에 서로 인접한 것.
#배추들이 모여있는 곳에는 배추흰나비가 한 마리만 있으면 되므로 서로 인접해 있는 배추들이 몇 군데에 퍼져있는지 조사하면 총 몇마리의 지렁이가 필요한가?


#입력
#첫 줄에는 테스트 케이스의 개수 : T
#그 다음 줄부터 
#각각의 테스트 케이스에 대해 첫째 줄에는 배추를 심은 배추밭의 가로 길이: M,세로 길이:N
#배추가 심어져 있는 위치의 개수 : K
#그 다음 K줄에는 배추의 위치 X,Y가 주어진다. 두 배추의 위치가 같은 경우는 없다.
#각 테스트 케이스에 대해 필요한 최소의 배추흰지렁이 마리 수를 출력한다.


import sys
from collections import deque
input = sys.stdin.readline

def bfs(x,y):
    queue = deque()
    queue.append((x,y))#큐에 x,y를 넣는다.
    matrix[y][x] = 2

    while queue:
        cx,cy = queue.popleft()#큐에서 빼서

        for i in range(4):
            nx = cx + dx[i]
            ny = cy+ dy[i]

            if 0<=nx<M and 0<=ny <N:#밭의 범위 안인가?
                if matrix[ny][nx] == 1:#배추가 있으면?
                    matrix[ny][nx] = 2 #방문처리
                    queue.append((nx,ny))



                


T = int(input())#테스트 케이스




dx = [-1,1,0,0]#가로 방향
dy = [0,0,-1,+1]#세로 방향


for _ in range(T):
    M,N,K = map(int,input().split())#M:가로, N:세로, K:배추가 심어져 있는 위치의 개수
    count=0
    matrix = [[0]*M for _ in range(N)] #밭(다 0으로 채움)
    for _ in range(K):
        X,Y = map(int,input().split())
        matrix[Y][X] = 1 #배추의 위치는 1로 바꿔주자.
    for x in range(0,M):
        for y in range(0,N):
            if matrix[y][x] == 1:
                bfs(x,y)
                count+=1
    print(count)






