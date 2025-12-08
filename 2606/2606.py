import sys
sys.setrecursionlimit(10**6)

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)



N = int(input())#컴퓨터의 수
M = int(input())#네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수
V = 1#시작 컴퓨터

graph = [ [] for _ in range(N+1)]

for _ in range(M):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1,N+1):
    graph[i].sort()

visited = [None]*(N+1)

dfs(V)

print(visited.count(True)-1)