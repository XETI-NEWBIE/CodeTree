# import sys
# # 파이썬은 재귀 깊이 제한이 기본적으로 낮아서 설정해 주는 것이 안전합니다.
# sys.setrecursionlimit(10**6)

def dfs(curr_node):
    # 현재 노드 방문 도장 쾅!
    visited[curr_node] = True
    
    # 현재 노드와 연결된 친구들을 하나씩 살펴봅니다.
    for next_node in graph[curr_node]:
        # 아직 방문하지 않은 친구라면?
        if not visited[next_node]:
            dfs(next_node) # 그 친구의 집으로 파고듭니다.

# N(정점 수), M(간선 수) 입력
n, m = map(int, input().split())

# 인접 리스트 생성 (1번부터 N번까지 사용하기 위해 n+1 크기로 만듦)
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

# 간선 정보 입력
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 1번 정점부터 탐색 시작
dfs(1)

# 방문한 정점 개수를 세고, 1번 정점(자기자신)은 뺍니다.
ans = sum(visited) - 1
print(ans)