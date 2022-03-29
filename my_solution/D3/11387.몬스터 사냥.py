def test3(D, L, N):
    cnt = 0
    damage = 0

    while cnt != N:
        damage += D * (1 + cnt * L * 0.01)
        cnt += 1

    return int(damage)


def main():
    T = int(input())

    for test_case in range(1, T + 1):
        D, L, N = map(int, input().split())
        answer = test3(D, L, N)

        print(f'#{test_case} {answer}')


if __name__ == '__main__':
    main()
