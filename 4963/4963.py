#풀이 전략
#1. 이중 for문으로 지도를 훑기
#2. 해당 지점이 땅(1)이면서 동시에 방문하지 않은 곳일 때만 BFS를 시작하자.
#3. BFS가 시작되면 연결된 모든 땅을 돌아다니는데, 이때 방문한 곳을 체크 해두자.
#4. 나중에 이중 for문을 돌다가 BFS로 이미 방문했던 좌표에 도달하면 여기는 아까 셌던 섬이구나 하면서 넘어가자.

import sys
from collections import deque #bfs를 쓰기 위해서 모듈 가져오기
input = sys.stdin.readline

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True

    while queue:
        x,y = queue.popleft()

        #8방향 확인하기
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            #[조건 1] matrix의 범위를 초과했을 시 무시하기
            if nx < 0 or ny < 0 or nx >=h  or ny >=w :
                continue

            #[조건 2] 바다일 경우 무시하기
            if matrix[nx][ny] == 0:
                visited[nx][ny] = True

            #[조건 3] 섬일 경우 -> 큐에 집어넣기
            if matrix[nx][ny] == 1 and visited[nx][ny] == False:
                visited[nx][ny] = True
                queue.append((nx,ny))
            
dx = [1, -1, 0, 0, 1, -1, 1, -1]  #열 좌표의 변화량
dy = [0, 0, 1, -1, 1, -1, -1, 1] #행 좌표의 변화량


while True:
    w,h = map(int,input().split()) #w:지도의 너비(가로=열), h:지도의 높이(세로=행)
    if w==0 and h==0:
        break
    count=0#섬의 개수
    matrix=[]   #바다와 섬 지도
    visited=[]  #바다와 섬 방문 지도
    
    for _ in range(h):#지도 입력
        matrix.append(list(map(int,input().split())))
    
    for _ in range(h):#방문 지도는 원소를 일단 False로 만들어놓자.
        visited.append([False]*w)

    #이제 matrix좌표를 하나씩 순회하면서 bfs를 실행하자

    for I in range(h):
        for J in range(w):
            if matrix[I][J] == 1 and visited[I][J] == False:
                count+=1
                bfs(I,J)

    print(count)

