def test3(N):
    # 첫 번째 숫자는 항상 1인 N 개의 행렬
    result = [[1] for _ in range(N)]
    # 2번째 행렬 2번째 숫자부터는 바로 윗 행렬 윗 숫자(num_right)와 그 왼쪽 숫자(num_left)의 합
    for i in range(1, N):
        for j in range(1, i + 1):
            num_left = result[i - 1][j - 1]
            try:
                # num_right 값이 존재하면 그 값을 이용
                num_right = result[i - 1][j]
            except IndexError:
                # 값이 없다면 0
                num_right = 0

            result[i].append(num_left + num_right)

    return result


def main():
    T = int(input())

    for test_case in range(1, T + 1):
        N = int(input())
        answer = test3(N)
        # 출력
        print(f'#{test_case}')
        for i in range(len(answer)):
            for j in range(len(answer[i])):
                print(answer[i][j], end=" ")
            print("")


if __name__ == '__main__':
    main()
