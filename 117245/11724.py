#방향 없는 그래프가 주어졌을 때, 연결 요소(Connected Component)의 개수를 구하는 프로그램을 작성하자.
#첫째 줄에 정점의 개수(N)과 간선의 개수(M)이 주어진다.
#둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다.
#같은 간선은 한 번만 주어진다.
#첫째 줄에 연결 요소의 개수를 출력한다.

import sys
from collections import deque #큐를 쓰려고

def bfs(n):
    queue = deque([n])
    visited[n] = True

    while queue:
        v = queue.popleft()

        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)


N,M = map(int,sys.stdin.readline().split()) #N:정점의 개수, M:간선의 개수

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1,N+1):
    graph[i].sort()

visited = [None]*(N+1)
count=0#연결 요소의 개수

for node in range(1,N+1):
    if not visited[node]:
        bfs(node)
        count+=1

print(count)





