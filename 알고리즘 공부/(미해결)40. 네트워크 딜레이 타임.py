import collections
import heapq

# 다익스트라 알고리즘으로 구현하기
# heapq를 이용 -> 추후 추가 공부!


def network(times: list[list[int]], N: int, K: int) -> int:
    # graph: defaultdict 에 넣기
    graph = collections.defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))

    # Q = K지점 까지 걸리는 시간
    Q = [(0, K)]
    dist = collections.defaultdict(int)

    while Q:
        print(Q)

        time, node = heapq.heappop(Q)
        if node not in dist:
            dist[node] = time
            for v, w in graph[node]:
                alt = time + w
                heapq.heappush(Q, (alt, v))
        print(dist)


    if len(dist) == N:
        return max(dist.values())

    return -1


def main():
    # [출발지 u, 도착지 v, 소요시간 w]
    times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    time = [[3, 1, 5], [3, 2, 2], [2, 1, 2], [3, 4, 1], [4, 5, 1], [5, 6, 1], [6, 7, 1], [7, 8, 1], [8, 1, 1]]
    # N = 노드 개수, K = 시작점
    N = 8
    K = 3

    answer = network(time, N, K)

    print(answer)


if __name__ == '__main__':
    main()
