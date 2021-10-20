def test3(L, U, X):
    if X < L:
        return L - X
    elif L < X < U:
        return 0
    else:
        return -1


def main():
    T = int(input())

    for test_case in range(1, T + 1):
        # L : 최소, U : 최대, X : 현재 운동량
        L, U, X = map(int, input().split())
        answer = test3(L, U, X)
        print(f'#{test_case} {answer}')


if __name__ == '__main__':
    main()
