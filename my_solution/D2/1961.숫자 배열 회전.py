def test3(input_list: list[list[int]]) -> list[list[int]]:
    # input_list 와 같은 N x N 배열 만들기
    result = []
    for _ in range(len(input_list)):
        result.append([])

    # 배열을 90도 회전하고 result: list 값에 넣기
    for j in range(len(input_list)):
        for i in range(len(input_list) - 1, -1, -1):
            result[j].append(input_list[i][j])

    return result


def main():
    # 테스트 케이스 입력
    T = int(input())

    for test_case in range(1, T + 1):
        # 반복 횟수
        N = int(input())
        # 배열 초기값 입력
        input_list = [list(map(int, input().split())) for _ in range(N)]
        # 90도, 180도, 270도 회전 배열
        answer_90 = test3(input_list)
        answer_180 = test3(answer_90)
        answer_270 = test3(answer_180)
        # 출력
        print(f'#{test_case}')
        for n in range(N):
            if n >= 1:
                print(" ")
            for k in range(N):
                print(f'{answer_90[n][k]}', end="")
            print(" ", end="")
            for j in range(N):
                print(f'{answer_180[n][j]}', end="")
            print(" ", end="")
            for l in range(N):
                print(f'{answer_270[n][l]}', end="")
        print("")


if __name__ == '__main__':
    main()
