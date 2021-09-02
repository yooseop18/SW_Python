def num_island(grid: list[list[str]]) -> int:
    def dfs(i, j):
        # 예외처리 및 땅이 아닌 경우 함수 종료
        if i < 0 or i >= len(grid) or \
                j < 0 or j >= len(grid[0]) or \
                grid[i][j] != '1':
            return

        # 탐색이 완료된 곳은 #으로 변경
        # 재탐색 시 중복 되지 않기 위해 1이 아닌 다른 값으로 변경
        grid[i][j] = '#'

        # 동서남북 탐색
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)

    count = 0

    # 육지를 탐색, dfs 함수로 연결여부 확인
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(i, j)
                count += 1

    return count


# 1: 육지, 0: 바다
grid1 = [
    ['1', '1', '1', '1', '0'],
    ['1', '1', '0', '1', '0'],
    ['1', '1', '0', '1', '0'],
    ['0', '0', '0', '1', '1'],
]


answer = num_island(grid1)

print(answer)