#문제
#1 : 집이 있는 곳, 0 : 집이 없는 곳
#연결 요소 완성하는 순서대로 1,2,3 이렇게 단지를 만들자. 
#단지의 개수
#단지의 개수에 속하는 아파트의 수를 출력해주자.


#풀이 전략
#섬의 개수 문제와 매우 비슷한 문제 다만 노드의 개수를 세야 함. + 오름차순

import sys
from collections import deque #BFS 구현하기 위한 큐
input = sys.stdin.readline


def bfs(x,y,cnt):

    queue = deque()
    queue.append((x,y))
    visited[x][y] = True #방문 처리

    while queue:

        x,y = queue.popleft()

        #4방향 확인하기
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >=N:#지도의 범위를 벗어남
                continue
            if matrix[nx][ny] == 0:#집이 없는 곳
                visited[nx][ny] = True#방문 처리
            if matrix[nx][ny] == 1 and visited[nx][ny] == False:#집이 있는 곳
                visited[nx][ny] = True#방문처리
                cnt +=1
                queue.append((nx,ny))
    return cnt

N = int(input())    #N*N의 지도의 크기(정사각형)

#방향 설정
dx = [-1,1,0,0]
dy = [0,0,-1,1]

matrix = []
visited = []#방문 지도
count1 = 0 #단지 수
count2=[]#단지의 아파트 개수를 넣을 배열
count_apartment=1#bfs 실행 전 자기자신의 아파트 단지를 포함해서 세주어야 한다.

for _ in range(N):#지도 입력
    matrix.append(list(map(int,input().strip())))

for _ in range(N):#방문 지도는 False로 초기화
    visited.append([False]*N)

for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1 and visited[i][j] == False:
            each_count = bfs(i,j,count_apartment)
            count2.append(each_count)
            count1+=1#단지의 개수
            
print(count1)
for i in sorted(count2):
    print(i)
            













