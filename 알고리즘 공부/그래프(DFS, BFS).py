graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3]
}


# DFS(재귀함수 이용)

# 재귀 함수 사용 시, 인자 값에 (discovered) 입력받지 않는 새로운 변수를 선언해서 사용하면 재귀로 사용가능
# 재귀 함수 시, 루프 탈출 문이 반드시 존재해야 함
# 리턴 리스트에 노드를 추가하고, 더이상 연결되어 있지 않으면 본 함수로 return
def recursive_dfs(v, discovered=[]):
    discovered.append(v)
    for w in graph[v]:
        if w not in discovered:
            discovered = recursive_dfs(w, discovered)

    return discovered


# DFS(스택 이용)
def iterative_dfs(start_v):
    discovered = []
    stack = [start_v]
    while stack:
        v = stack.pop()
        if v not in discovered:
            discovered.append(v)
            for w in graph[v]:
                stack.append(w)

    return discovered


# BFS -> 무조건 큐를 이용해야함
def iterative_bfs(start_v):
    discovered = [start_v]
    queue = [start_v]
    while queue:
        v = queue.pop(0)
        for w in graph[v]:
            if w not in discovered:
                discovered.append(w)
                queue.append(w)

    return discovered


print(f'recursive dfs: {recursive_dfs(1)}')
print(f'iterative dfs: {iterative_dfs(1)}')
print(f'iterative bfs: {iterative_bfs(1)}')





