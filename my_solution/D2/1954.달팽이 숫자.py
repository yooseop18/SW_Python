def snail_num(N: int) -> list[int]:
    arr = []
    for i in range(N - 1):
        for j in range(N - 1):
            arr[i][j].append(-1)

    return arr


def main():
    T = int(input())

    for test_case in range(1, T + 1):
        N = int(input())
        answer = snail_num(N)
        print(f'#{test_case} {answer}')


main()

