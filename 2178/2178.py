import sys
from collections import deque #최단 거리를 구할 때는 BFS

def bfs(x,y):
    queue = deque()
    queue.append((x,y)) #큐에는 (x,y) 좌표 튜플을 넣자.

    while queue:
        x,y = queue.popleft()

        #4방향 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            #미로 공간을 벗어난다면[조건 1]
            if nx < 0 or nx >=N or ny<0 or ny>=M:
                continue #이번 방향은 패스
            #벽인 경우 무시(0은 벽)
            if graph[nx][ny] == 0:
                continue #패스

            #해당 노드를 처음 방문하는 경우에만 (1인 경우에만)
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1 
                
                queue.append((nx,ny))
    
    return graph[N-1][M-1]


N,M = map(int,sys.stdin.readline().split()) #N*M크기의 격자

graph = []

for _ in range(N):#N개의 줄에 M개의 정수를 배열로 저장
    graph.append(list(map(int,sys.stdin.readline().strip())))

#상하좌우 방향 정의
dx = [-1,1,0,0]
dy = [0,0,-1,1]

X=0
Y=0
print(bfs(X,Y))




