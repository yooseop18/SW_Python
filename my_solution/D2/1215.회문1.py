def test3(N, arr):
    result = 0
    # 가로, 세로로 탐색
    for i in range(8):
        start = 0
        while 8 - start >= N:
            check_arr1, check_arr2 = [], []
            for j in range(start, N + start):
                check_arr1.append(arr[i][j]), check_arr2.append(arr[j][i])
            # 회문 판별
            re1, re2 = reversed(check_arr1), reversed(check_arr2)
            if check_arr1 == list(re1):
                result += 1
            if check_arr2 == list(re2):
                result += 1
            # 시작점 1 증가
            start += 1
            continue

    return result


def main():

    for test_case in range(1, 11):
        N = int(input())
        arr = [list(input()) for _ in range(8)]
        answer = test3(N, arr)
        print(f'#{test_case} {answer}')


if __name__ == '__main__':
    main()
