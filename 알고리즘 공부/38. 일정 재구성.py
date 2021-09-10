import collections


def find_path(tickets: list[list[str]]) -> list[str]:
    graph = collections.defaultdict(list)
    # dic 형식으로 입력값 저장 뒤 정렬
    for a, b in sorted(tickets):
        graph[a].append(b)
    print(graph)
    result = []

    # DFS 탐색, 재귀 호출로 각 key 의 value 값을 result 에 append
    def dfs(a):
        while graph[a]:
            dfs(graph[a].pop(0))

        result.append(a)
        print(result)

    dfs("J")
    # result 에는 경로 반대로 입력되었으므로, 반대로 출력
    return result[::-1]


def main():
    tickets1 = [["M", "L"], ["J", "M"], ["SF", "SJ"], ["L", "SF"]]
    tickets2 = [
        ["J", "SF"], ["J", "A"],
        ["SF", "A"], ["A", "J"], ["A", "SF"]
    ]

    print(f'{find_path(tickets1)}')
    # print(f'{find_path(tickets2)}')


if __name__ == '__main__':
    main()

