# 현재 풀이는 brutal force 임, BFS 로 풀이 가능
# DP 로 풀 수 있음. 나중에 공부 뒤 다시 구현해보기

def test3(arr, M):
    max_sum, i_start, j_start = 0, 0, 0
    while True:
        arr_sum = 0
        # 파리채로 잡은 파리 수 합산
        for i in range(i_start, i_start + M):
            for j in range(j_start, j_start + M):
                arr_sum += arr[i][j]
        # max 값 갱신
        if arr_sum > max_sum:
            max_sum = arr_sum

        # j 범위 내 j_start 값 증가하면서 재탐색
        if j_start != len(arr) - M:
            j_start += 1
            continue
        # i 범위 내 i 값 추가하고 다시 재탐색
        else:
            if i_start != len(arr) - M:
                i_start += 1
                j_start = 0
                continue
            else:
                break


    return max_sum


def main():
    T = int(input())

    for test_case in range(1, T + 1):
        N, M = map(int, input().split())
        arr = [list(map(int, input().split())) for _ in range(N)]
        answer = test3(arr, M)
        print(f'#{test_case} {answer}')


if __name__ == '__main__':
    main()
