import sys
sys.setrecursionlimit(10**6)#DFS로 깊게 들어가려면 이 제한을 반드시 늘려줘야 한다.
from collections import deque


def dfs(v):#깊이 우선 탐색(재귀로 구현)
    
    visited1[v] = True #방문 처리
    print(v, end=' ')

    for i in graph[v]:
        if not visited1[i]:
            dfs(i)

def bfs(start_v):#너비 우선 탐색

    queue=deque([start_v])#큐를 만들고 시작점을 넣는다.

    visited2[start_v] = True#시작점 방문 표시

    while queue:
        #큐의 맨 앞쪽(왼쪽)에서 하나 꺼낸다.(pop)
        v = queue.popleft()
        print(v,end=' ')

        for i in graph[v]:
            if not visited2[i]:
                visited2[i] = True
                queue.append(i)

#N : 정점 개수, M : 간선 개수, V : 탐색을 시작할 정점의 번호
N,M,V = map(int,sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]#인접 리스트 생성(1번~N번을 쓰기 위해 N+1 크기로 지정)

for _ in range(M):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)#양방향 연결

for i in range(1,N+1):#오름차순으로 정렬
    graph[i].sort()

#방문 기록표 만들기(False로 초기화)
visited1 = [False] * (N+1)
visited2 = [False] * (N+1)

dfs(V)
print()
bfs(V)


