import collections


def test3(arr):
    # 가로, 세로 스도쿠 여부 확인
    for i in range(9):
        horizontal_arr = collections.defaultdict(int)
        width_arr = collections.defaultdict(int)
        for j in range(9):
            horizontal_arr[arr[i][j]] += 1
            width_arr[arr[j][i]] += 1
        # 스도쿠 아니라면 0 리턴
        for check in range(1, 10):
            if horizontal_arr[check] == 0 or width_arr[check] == 0:
                return 0

    # 3x3 스도쿠 여부 확인
    # arr[i][j] 에서 i +=3 씩 증가, j += 3 씩 증가 -> i_cnt, j_cnt
    # j의 시작점 선언 뒤 3씩 증가 -> start_j
    start_j = 0
    while start_j != 9:
        i_cnt = 0
        while i_cnt != 9:
            square_arr = collections.defaultdict(int)
            for k in range(i_cnt, i_cnt + 3):
                j_cnt = 0

                while j_cnt != 9:
                    for l in range(j_cnt + start_j, j_cnt + start_j + 3):
                        square_arr[arr[k][l]] += 1
                        j_cnt += 3

            i_cnt += 3
            # 스도쿠 아니라면 0 리턴
            for check in range(1, 10):
                if square_arr[check] == 0:
                    return 0

        start_j += 3
    # 최종적으로 스도쿠가 맞으면, 1 리턴
    return 1


def main():
    T = int(input())

    for test_case in range(1, T + 1):
        arr = [list(map(int, input().split())) for _ in range(9)]
        answer = test3(arr)
        print(f'#{test_case} {answer}')


if __name__ == '__main__':
    main()