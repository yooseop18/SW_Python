
def test3(N, PD, PG):
    # N = 오늘 최대 게임 수, D = 오늘 한 게임 수, G = 전체 게임수
    # PD = D판 중 승률, PG = G판 중 승률
    if PG == 100 and PD != 100:
        return "Broken"
    if PG == 0 and PD != 0:
        return "Broken"

    for n in range(1, N + 1):
        # 오늘의 승률이 정수인지 확인
        if (n * PD / 100) == (n * PD // 100):
            print(f'{n * PD / 100}')
            return "Possible"
            break

    return "Broken"


def main():
    T = int(input())

    for test_case in range(1, T + 1):
        N, PD, PG = map(int, input().split())
        # input = 최대 판수, 오늘 승률, 전체 승률
        answer = test3(N, PD, PG)
        print(f'#{test_case} {answer}')


if __name__ == '__main__':
    main()
